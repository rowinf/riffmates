import logging

from django.contrib.auth.signals import user_login_failed
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.db.models.signals import post_save
from django.dispatch import receiver

from bands.forms import VenueForm, MusicianForm
from bands.models import Musician, Band, Venue, UserProfile


def musicians(request):
    all_musicians = Musician.objects.all().order_by("last_name")
    page_num = int(request.GET.get("page", 1))
    try:
        per_page = int(request.GET.get("per_page", 2))
    except Exception as _:
        per_page = 2

    paginator = Paginator(all_musicians, per_page)
    if page_num < 1:
        page_num = 1
    elif page_num > paginator.num_pages:
        page_num = paginator.num_pages

    page = paginator.page(page_num)
    data = {"musicians": page.object_list, "page": page, "paginator": paginator}

    return render(request, "musicians.html", data)


def musician(request, musician_id):
    musician_showing = get_object_or_404(Musician, id=musician_id)
    data = {"musician": musician_showing}
    return render(request, "musician.html", data)


@login_required
def edit_musician(request, musician_id=0):
    if musician_id != 0:
        musician_editing = get_object_or_404(Musician, id=musician_id)
        if not request.user.userprofile.musician_profiles.filter(id=musician_id).exists():
            raise Http404("Musician not permitted")

    if request.method == "GET":
        if musician_id == 0:
            form = MusicianForm()
        else:
            form = MusicianForm(request.POST, instance=musician_editing)
    else:
        if musician_id == 0:
            musician_editing = Musician.objects.create()
        form = MusicianForm(request.POST, request.FILES, instance=musician_editing)

        if form.is_valid():
            musician_editing = form.save()
            request.user.userprofile.musician_profiles.add(musician_editing)
            return redirect("musician", musician_id=musician_editing.id)
    return render(request, "edit_musician.html", {"form": form})


def bands(request):
    bands = Band.objects.all().order_by("name")
    page_num = int(request.GET.get("page", 1))
    try:
        per_page = int(request.GET.get("per_page", 2))
    except Exception as _:
        per_page = 2

    paginator = Paginator(bands, per_page)
    if page_num < 1:
        page_num = 1
    elif page_num > paginator.num_pages:
        page_num = paginator.num_pages

    page = paginator.page(page_num)
    data = {"bands": page.object_list, "page": page, "paginator": paginator}

    return render(request, "bands.html", data)


def band(request, band_id):
    band = get_object_or_404(Band, id=band_id)
    musicians = band.musicians.all()
    data = {"band": band, "musicians": musicians}

    return render(request, "band.html", data)


def venues(request):
    all_venues = Venue.objects.all().order_by("name")
    profile = getattr(request.user, "userprofile", None)
    if profile:
        for venue in all_venues:
            venue.controlled = profile.venues_controlled.filter(id=venue.id).exists()

    page_num = int(request.GET.get("page", 1))
    try:
        per_page = int(request.GET.get("per_page", 2))
    except Exception as _:
        per_page = 2

    paginator = Paginator(all_venues, per_page)
    if page_num < 1:
        page_num = 1
    elif page_num > paginator.num_pages:
        page_num = paginator.num_pages

    page = paginator.page(page_num)
    data = {"venues": page.object_list, "page": page, "paginator": paginator}

    return render(request, "venues.html", data)


def venue(request, venue_id):
    venue = get_object_or_404(Venue, id=venue_id)
    rooms = venue.room_set.all()  # pyright: ignore
    data = {"venue": venue, "rooms": rooms}

    return render(request, "venue.html", data)


@login_required
def restricted_page(request):
    data = {
        'title': 'Restricted Page',
        'content': '<h1>You are logged in</h1>',
    }

    return render(request, "general.html", data)


@login_required
def musician_restricted(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id)
    profile = request.user.userprofile
    allowed = False

    if profile.musician_profiles.filter(id=musician_id).exists():
        allowed = True
    else:
        # User is not this musician, check if they're a bandmate
        musician_profiles = set(
            profile.musician_profiles.all()
        )
        for band in musician.band_set.all():
            band_musicians = set(band.musicians.all())
            if musician_profiles.intersection(band_musicians):
                allowed = True
                break

    if not allowed:
        raise Http404("Permission denied")

    content = f"""
        <h1>Musician Page: {musician.last_name}</h1>
    """
    data = {
        'title': 'Musician Restricted',
        'content': content,
    }

    return render(request, "general.html", data)


@user_passes_test(lambda u: u.is_authenticated and u.userprofile.venues_controlled.exists())
def venues_restricted(request):
    return venues(request)


@receiver(post_save, sender=User)
def user_post_save(sender, **kwargs):
    # Create UserProfile object if User object is new
    # and not loaded from fixture
    if kwargs['created'] and not kwargs['raw']:
        user = kwargs['instance']
        try:
            # Double check UserProfile doesn't exist already
            # (admin might create it before the signal fires)
            UserProfile.objects.get(user=user)

        except UserProfile.DoesNotExist:
            # No UserProfile exists for this user, create one
            UserProfile.objects.create(user=user)


@receiver(user_login_failed)
def _user_login_failed(sender, request, **kwargs):
    logging.warn(f"login failed {kwargs['credentials']['username']} {request.GET['next']}")


@login_required
def edit_venue(request, venue_id=0):
    if venue_id != 0:
        venue = get_object_or_404(Venue, id=venue_id)
        if not request.user.userprofile.venues_controlled.filter(id=venue_id).exists():
            raise Http404("Can only edit controlled venues")

    if request.method == 'GET':
        if venue_id == 0:
            form = VenueForm()
        else:
            form = VenueForm(instance=venue)

    else:  # POST
        if venue_id == 0:
            venue = Venue.objects.create()

        form = VenueForm(request.POST, request.FILES, instance=venue)

        if form.is_valid():
            venue = form.save()

            # Add the venue to the user's profile
            request.user.userprofile.venues_controlled.add(venue)
            return redirect("venues")

    # Was a GET, or Form was not valid
    data = {
        "form": form,
        "rooms": venue.room_set.all()
    }

    return render(request, "edit_venue.html", data)

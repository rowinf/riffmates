from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    musician = get_object_or_404(Musician, id=musician_id)
    data = {"musician": musician}

    return render(request, "musician.html", data)


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
    venues = Venue.objects.all().order_by("name")
    page_num = int(request.GET.get("page", 1))
    try:
        per_page = int(request.GET.get("per_page", 2))
    except Exception as _:
        per_page = 2

    paginator = Paginator(venues, per_page)
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
        # User is not this musician, check if they're a band-mate
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
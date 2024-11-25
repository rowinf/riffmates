from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

from bands.models import Musician, Band, Venue


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
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator

from bands.models import Musician


def musicians(request):
    data = {"musicians": Musician.objects.all().order_by("last_name")}
    paginator = Paginator(all_musicians, 2)
    return render(request, "musicians.html", data)


def musician(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id)
    data = {"musician": musician}

    return render(request, "musician.html", data)

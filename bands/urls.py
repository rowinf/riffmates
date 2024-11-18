# RiffMates/bands/urls.py
from django.urls import path

from bands import views

urlpatterns = [
    path("musician/<int:musician_id>/", views.musician, name="musician"),
    path("musicians/", views.musicians, name="musicians"),
    path("", views.bands, name="bands"),
    path("<int:band_id>", views.band, name="band"),
]

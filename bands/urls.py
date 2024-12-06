# RiffMates/bands/urls.py
from django.urls import path

from bands import views

urlpatterns = [
    path("musician/<int:musician_id>/edit", views.edit_musician, name="edit_musician"),
    path("musician/<int:musician_id>/", views.musician, name="musician"),
    path("musicians/", views.musicians, name="musicians"),
    path("bands/", views.bands, name="bands"),
    path("<int:band_id>", views.band, name="band"),
    path("venues/", views.venues, name="venues"),
    path("venues_restricted/", views.venues_restricted, name="venues_restricted"),
    path("venue/<int:venue_id>", views.venue, name="venue"),
    path("venue/<int:venue_id>/edit", views.edit_venue, name="edit_venue"),
    path("restricted_page/", views.restricted_page, name="restricted_page"),
]

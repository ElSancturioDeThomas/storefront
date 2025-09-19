from django.contrib import admin
from django.urls import include, path

from . import views

app_name = "listings"

urlpatterns = [
    path("", views.index, name="index"),
    path("listing/<int:listing_id>/", views.view_listing, name="view_listing"),
    path("listing/<int:listing_id>/place_bid/", views.place_bid, name="place_bid"),
    path("listing/<int:listing_id>/comment/", views.comment, name="comment"),
    path("listing/<int:listing_id>/close/", views.close_listing, name="close_listing"),
    path("listing/<int:listing_id>/is_closed/", views.is_closed, name="is_closed"),
    path("listing/<int:listing_id>/remove/", views.remove_listing, name="remove_listing"),
]
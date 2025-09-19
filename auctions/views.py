from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import User, Watchlist
from listings.models import Listing, Bid



def index(request):
    return render(request, "auctions/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("listings:index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("listings:index"))

@csrf_exempt
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("listings:index"))
    else:
        return render(request, "auctions/register.html")

def create_listing(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        image_url = request.POST["image_url"]
        category = request.POST["category"]
        starting_bid = request.POST["starting_bid"]
        user = request.user
        listing = Listing.objects.create(title=title, description=description, image_url=image_url, category=category, user=user)
        starting_bid = Bid.objects.create(listing=listing, user=user, current_bid=starting_bid, bid_required=starting_bid)
        return HttpResponseRedirect(reverse("listings:view_listing", args=[listing.id]))
    return render(request, "auctions/create_listing.html")


def add_to_watchlist(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    if not Watchlist.objects.filter(listing=listing, user=request.user).exists():
        Watchlist.objects.create(listing=listing, user=request.user)

    return HttpResponseRedirect(reverse("listings:view_listing", args=[listing_id]))

def delete_from_watchlist(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    watchlist = Watchlist.objects.get(listing=listing, user=request.user)
    watchlist.delete()
    return HttpResponseRedirect(reverse("listings:view_listing", args = [listing_id]))

def watchlist(request):
    watchlist = Watchlist.objects.filter(user=request.user)
    return render(request, "auctions/watchlist.html", {
        "watchlist": watchlist,
    })

def category_bar(request):
    categories = Listing.objects.values('category').distinct()
    return render(request, "auctions/category.html", {
        "categories": categories,
        "show_categories": True,
    })

def category_page(request, category):
    listings = Listing.objects.filter(category=category)
    return render(request, "auctions/category.html", {
        "listings": listings,
        "category_name": category,
        "show_categories": False,
    })
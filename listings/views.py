from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Listing, Bid, Comment

# Create your views here.

def index(request):
    listings = Listing.objects.all()
    return render(request, "listings/index.html", {
        "listings": listings,
    })

def view_listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    bid = Bid.objects.filter(listing=listing).order_by('-current_bid').first()
    
    # Check if the listing is in the user's watchlist
    in_watchlist = False
    if request.user.is_authenticated:
        from auctions.models import Watchlist
        in_watchlist = Watchlist.objects.filter(listing=listing, user=request.user).exists()
    
    return render(request, "listings/listing.html", {
        "listing": listing,
        "bid": bid,
        "in_watchlist": in_watchlist,
        "is_closed": not listing.active
    })

def place_bid(request, listing_id):
    if request.method == "POST":
        bid_amount = float(request.POST.get("bid_amount"))
        listing = Listing.objects.get(id=listing_id)
        bid = Bid.objects.filter(listing=listing).order_by('-current_bid').first()

        current_bid_amount = bid.current_bid if bid else 0

        if bid_amount <= current_bid_amount:
            messages.error(request, "Bid must be greater than the current bid")
        else:
            bid = Bid.objects.create(
                listing=listing,
                user=request.user,
                current_bid=bid_amount,
                bid_required=bid_amount + 5
            )
            messages.success(request, "Bid placed successfully!")
    return render(request, "listings/listing.html", {
        "listing": listing,
        "bid": bid
    })



def comment(request, listing_id):
    if request.method == "POST":
        comment_text = request.POST.get("comment_text")
        listing = Listing.objects.get(id=listing_id)
        if comment_text:
            Comment.objects.create(
                listing=listing,
                user=request.user,
                comment=comment_text
            )
            messages.success(request, "Comment added successfully!")

    return redirect("listings:view_listing", listing_id=listing_id)

def close_listing(request, listing_id):
    if request.method == "POST":
        listing = Listing.objects.get(id=listing_id)
        
        
        if listing.user == request.user:
            listing.active = False
            listing.save()

    return redirect("listings:view_listing", listing_id=listing_id)

def is_closed(listing_id):
    closed = Listing.objects.filter(id=listing_id, active=False).exists()

    return closed

def remove_listing(request, listing_id):
    if request.method == "POST":
        listing = Listing.objects.get(id=listing_id)
        listing.delete()
    return redirect("listings:index")
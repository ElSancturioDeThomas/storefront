from django.contrib import admin
from .models import Listing, Bid, Comment
# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "comment", "listing")
    list_filter = ("user", "listing")
    search_fields = ("user", "comment", "listing")

admin.site.register(Comment, CommentAdmin)

class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "image_url", "category", "user", "date_created", "active")
    list_filter = ("category", "user", "date_created", "active")
    search_fields = ("title", "description", "category", "user")

admin.site.register(Listing, ListingAdmin)

class BidAdmin(admin.ModelAdmin):
    list_display = ("listing", "user", "current_bid", "bid_required", "bid_date")
    list_filter = ("listing", "user", "bid_date")
    search_fields = ("listing", "user", "current_bid", "bid_required")

admin.site.register(Bid, BidAdmin)
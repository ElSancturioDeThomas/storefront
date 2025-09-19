from django.db import models
from auctions.models import User
# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models


class Listing(models.Model):
    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('fashion', 'Fashion'),
        ('home', 'Home & Garden'),
        ('vehicles', 'Vehicles'),
        ('collectibles', 'Collectibles'),
        ('sports', 'Sports & Recreation'),
        ('books', 'Books & Media'),
        ('art', 'Art & Antiques'),
        ('jewelry', 'Jewelry & Watches'),
        ('toys', 'Toys & Games'),
        ('other', 'Other'),
    ]
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auction_listings")
    date_created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id} {self.title} {self.description}"

class Bid(models.Model):
    bid_id = models.BigAutoField(primary_key=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="item")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bids")
    current_bid = models.DecimalField(max_digits=10, decimal_places=2)
    bid_required = models.DecimalField(max_digits=10, decimal_places=2)
    bid_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bid_id} {self.listing.title} {self.user.username} {self.current_bid}"

class Comment(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comment")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    comment = models.TextField(max_length=255)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment_id} {self.listing.title} {self.user.username} {self.comment}"
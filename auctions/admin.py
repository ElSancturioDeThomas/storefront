from django.contrib import admin
from .models import User, Watchlist

# Register your models here.

admin.site.register(User)

class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'listing')
    search_fields = ('user', 'listing')
    list_filter = ('user', 'listing')
    ordering = ('-id',)


admin.site.register(Watchlist, WatchlistAdmin)
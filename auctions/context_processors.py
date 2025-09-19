from .models import Watchlist

def watchlist_count(request):
    """
    Context processor to add watchlist count to all templates.
    """
    if request.user.is_authenticated:
        count = Watchlist.objects.filter(user=request.user).count()
    else:
        count = 0
    
    return {
        'watchlist_count': count
    }
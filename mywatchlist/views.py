from django.shortcuts import render
from mywatchlist.models import watchlistItem

# Create your views here.
def show_watchlist(request):
    data_barang_watchlist = watchlistItem.objects.all()
    context = {
        'list_barang' : data_barang_watchlist,
        'nama' : "Salma Hanifah"
    }
    return render(request, "mywatchlist.html", context)

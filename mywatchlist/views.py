from django.shortcuts import render
from mywatchlist.models import watchlistItem
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist(request):
    data_barang_watchlist = watchlistItem.objects.all()
    context = {
        'list_barang' : data_barang_watchlist,
        'nama' : "Salma Hanifah"
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = watchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = watchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml_by_id(request, id):
    data = watchlistItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = watchlistItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
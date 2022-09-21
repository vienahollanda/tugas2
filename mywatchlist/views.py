from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.core import serializers
from django.http import HttpResponse
# TODO: Create your views here.

def show_mywatchlist(request):
    data_mywatchlist = MyWatchList.objects.all()
    context = {
        'list_film': data_mywatchlist,
        'nama': 'Viena Hollanda Koswara',
        'NPM': '2106751253',
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

def show_json(request):  
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")


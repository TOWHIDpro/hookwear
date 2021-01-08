from django.shortcuts import render
from . models import selldata

# Create your views here.

def index(request):

    sells = selldata.objects.all()

    return render(request, "index/index.html", {
        'sells': sells
    })
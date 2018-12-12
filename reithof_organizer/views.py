from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'reithof_organizer/ritterstall.html')

def ueber_uns(request):
    return render(request, 'reithof_organizer/ueber_uns.html')

def kurse(request):
    return render(request, 'reithof_organizer/kurse.html')

def galerie(request):
    return render(request, 'reithof_organizer/galerie.html')

def unsere_pferde(request):
    return render(request, 'reithof_organizer/unsere_pferde.html')

def facebooknews(request):
    return render(request, 'reithof_organizer/facebooknews.html')
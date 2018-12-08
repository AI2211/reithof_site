from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'reithof_organizer/unser_stall.html')

def ueber_uns(request):
    return render(request, 'reithof_organizer/ueber_uns.html')

def aktuell(request):
    return render(request, 'reithof_organizer/aktuell.html')

def galerie(request):
    return render(request, 'reithof_organizer/galerie.html')

def unsere_pferde(request):
    return render(request, 'reithof_organizer/unsere_pferde.html')
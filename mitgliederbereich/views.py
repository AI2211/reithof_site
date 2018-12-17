from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'mitgliederbereich/index.html')

def mistplan(request):
    return render(request, 'mitgliederbereich/mistplan.html')

def standortPferde(request):
    return render(request, 'mitgliederbereich/standortPferde.html')

def termine(request):
    return render(request, 'mitgliederbereich/termine.html')


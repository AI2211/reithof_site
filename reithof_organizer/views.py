from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import UserCreationForm

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

def register(request):
    profile_form = UserCreationForm(request.POST or None)
    if request.method == "POST" and profile_form.is_valid():
        # user = profile_form.save(commit=False)
        # vorname = profile_form.cleaned_data['vorname']
        # nachname = profile_form.cleaned_data['nachname']
        # email = profile_form.cleaned_data['email']
        # passwort = profile_form.cleaned_data['password1']
        # user.set_password(passwort)
        profile_form.save()
    context = {
        "profile_form": profile_form,
        }
    return render(request, 'reithof_organizer/register.html', context)


# fields = ['vorname', 'nachname', 'email', 'passwort', 'geburtsdatum', 'mistpunkte']
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.mail import send_mail

from reithof_site import settings
from .forms import ProfileForm
from .models import Profile
#import requests

def index(request):
    return render(request, 'reithof_organizer/ritterstall.html')

#def index(request):
    #r = requests.get('http://httpbin.org/status/418')
    #print(r.text)
    #return render(request, '<pre>' + r.text + '</pre>')

def ueber_uns(request):
    all_profiles = Profile.objects.all()
    context = {'all_profiles': all_profiles}
    return render(request, 'reithof_organizer/ueber_uns.html', context)

def kurse(request):
    return render(request, 'reithof_organizer/kurse.html')

def galerie(request):
    return render(request, 'reithof_organizer/galerie.html')

def unsere_pferde(request):
    return render(request, 'reithof_organizer/unsere_pferde.html')

def facebooknews(request):
    return render(request, 'reithof_organizer/facebooknews.html')

def register(request):
    if request.method == "POST":
        profile_form = ProfileForm(request.POST or None)
        if profile_form.is_valid():
            user = profile_form.save(commit=False)
            vorname = profile_form.cleaned_data['vorname']
            nachname = profile_form.cleaned_data['nachname']
            email = profile_form.cleaned_data['email']
            #send_mail('Hello from Test', 'Hello I am Test', settings.EMAIL_HOST_USER, [email], fail_silently=False)
            profile_form.save()
            return redirect('login')
    else:
        profile_form = ProfileForm()
    return render(request, 'reithof_organizer/register.html', {'profile_form': profile_form})
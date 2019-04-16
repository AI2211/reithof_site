from django.http import HttpResponse
from django.contrib.auth.forms import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from .forms import EmailChangeForm, ProfileChangeForm

from reithof_organizer.models import *

def index(request):
    return render(request, 'mitgliederbereich/base.html')

def profil(request):
    all_profiles = Profile.objects.all()
    return render(request, 'mitgliederbereich/profil.html', {'all_profiles': all_profiles})

def edit_profil(request):
    if request.method == 'POST':
        form = ProfileChangeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edit_profil_success')
    else:
        form = ProfileChangeForm()
    return render(request, 'mitgliederbereich/edit_profil.html', {'form': form})


def profile_set_active(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    profile.is_active = True
    profile.save()

    return render(request, 'mitgliederbereich/activated_user.html', {'profile': profile})

def profile_set_not_active(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    profile.is_active = False
    profile.save()

    return render(request, 'mitgliederbereich/deactivated_user.html', {'profile': profile})

def profile_set_staff(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    profile.is_staff = True
    profile.save()

    return render(request, 'mitgliederbereich/is_staff_user.html',  {'profile': profile})


def profile_set_not_staff(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    profile.is_staff = False
    profile.save()

    return render(request, 'mitgliederbereich/is_not_staff_user.html',  {'profile': profile})

def profile_delete(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    profile.delete()

    return render(request, 'mitgliederbereich/deleted_user.html',  {'profile': profile})

def email_change(request):
    if request.method == 'POST':
        form = EmailChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('email_change_done')
    else:
        form = EmailChangeForm(request.user)
    return render(request, 'mitgliederbereich/email_change.html', {'form': form})

def email_change_done(request):
    return render(request, 'mitgliederbereich/email_change_done.html')

def pferde_management(request):
    all_user_pferde = Pferd.objects.all().filter(besitzer=request.user)
    return render(request, 'mitgliederbereich/pferde_management.html', {'all_user_pferde': all_user_pferde})

def pferd_standort(reqiest, pk):
    pferd =get_object_or_404(Pferd, pk=pk)

    return render(reqiest, 'mitgliederbereich/pferd_standort.html', {'pferd': pferd})

def set_mistpunkte_to_user(request, points):
    profile = get_object_or_404(Profile, pk=request.user.pk)
    profile.set_mistpunkte(points)

    return render(request, 'mitgliederbereich/profil.html')

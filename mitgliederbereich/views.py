from django.shortcuts import render, get_object_or_404, redirect
from .forms import EmailChangeForm, ProfileChangeForm, AddPferdForm, EditPferdForm
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.utils.dateparse import parse_date

from django.contrib.auth.decorators import login_required


from webauftritt.models import *

from django.views import generic  # Calendar
from django.utils.safestring import mark_safe  # Calendar
from datetime import datetime, timedelta, date  # Calendar
from django.http import HttpResponse, HttpResponseRedirect  # Calendar
from django.urls import reverse  # Calendar

from .models import Event  # Calendar
from .models import nameMistplan
# from .models import nameMistplan
from .utils_Calendar import Calendar  # Calendar
from django import forms
from .forms import EventForm  # Calendar
import calendar  # Calendar

@login_required
def index(request):
    return render(request, 'mitgliederbereich/base.html')

@login_required
def profil(request):
    all_profiles = Profile.objects.all()
    return render(request, 'mitgliederbereich/profil.html', {'all_profiles': all_profiles})

@login_required
def edit_profil(request):
    if request.method == 'POST':
        form = ProfileChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('edit_profil_success')
    else:
        form = ProfileChangeForm()
    return render(request, 'mitgliederbereich/edit_profil.html', {'form': form})

@login_required
def edit_profil_success(request):
    return render(request, 'mitgliederbereich/edit_profil_success.html')

@login_required
def profile_set_active(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    profile.is_active = True
    profile.save()

    return render(request, 'mitgliederbereich/activated_user.html', {'profile': profile})

@login_required
def profile_set_not_active(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    profile.is_active = False
    profile.save()

    return render(request, 'mitgliederbereich/deactivated_user.html', {'profile': profile})

@login_required
def profile_set_staff(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    profile.is_staff = True
    profile.save()

    return render(request, 'mitgliederbereich/is_staff_user.html', {'profile': profile})

@login_required
def profile_set_not_staff(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    profile.is_staff = False
    profile.save()

    return render(request, 'mitgliederbereich/is_not_staff_user.html', {'profile': profile})

@login_required
def profile_delete(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    profile.delete()

    return render(request, 'mitgliederbereich/deleted_user.html', {'profile': profile})

@login_required
def email_change(request):
    if request.method == 'POST':
        form = EmailChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('email_change_done')
    else:
        form = EmailChangeForm(request.user)
    return render(request, 'mitgliederbereich/email_change.html', {'form': form})

@login_required
def email_change_done(request):
    return render(request, 'mitgliederbereich/email_change_done.html')

@login_required
def pferde_management(request):
    all_user_pferde = Pferd.objects.all().filter(besitzer=request.user)

    if request.method == "POST":
        form = AddPferdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = AddPferdForm()
    else:
        form = AddPferdForm()

    return render(request, 'mitgliederbereich/pferde_management.html', {'all_user_pferde': all_user_pferde, 'form': form})

@login_required
def meine_kurse(request):
    profile = get_object_or_404(Profile, pk=request.user.pk)
    all_user_kurse = profile.Kurse.all()

    return render(request, 'mitgliederbereich/kurse.html', {'kurse': all_user_kurse})


@login_required
def pferd_standort(reqiest, pk):
    pferd = get_object_or_404(Pferd, pk=pk)

    return render(reqiest, 'mitgliederbereich/pferd_standort.html', {'pferd': pferd})

@login_required
def set_mistpunkte_to_user(request, points):
    profile = get_object_or_404(Profile, pk=request.user.pk)
    profile.set_mistpunkte(points)

    return render(request, 'mitgliederbereich/profil.html')


class CalendarView(generic.ListView):  # Calendar
    model = Event
    template_name = 'mitgliederbereich/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


class MistplanView(generic.ListView):
    model = Event
    template_name = 'mitgliederbereich/mistplan.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonthMistplan()
        context['mistplan'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def prev_month(d):  # Calendar
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):  # Calendar
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def get_date(req_day):  # Calendar
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'mitgliederbereich/event.html', {'form': form})


#@csrf_exempt
@method_decorator(csrf_exempt, name='dispatch')
class MistplanDetail(View):

    def post(self, request, *args, **kwargs):
        if request.method != 'POST':
            return HttpResponse(status=405)

        cal_date = parse_date(kwargs['date'])
        horse_power = kwargs['horsePower']
        username = request.user.get_full_name()

        nameMistplan.objects.create(user=request.user, date=cal_date, horsepower=horse_power)

        data = {
            'name': username
        }
        return JsonResponse(data)


def delete_pferd(request, pk):
    pferd = get_object_or_404(Pferd, pk=pk)
    pferd.delete()

    return render(request, 'mitgliederbereich/deleted_pferd.html', {'pferd': pferd})

def edit_pferd(request, pk):
    pferd = get_object_or_404(Pferd, pk=pk)
    if request.method == 'POST':
        form = EditPferdForm(request.POST, instance=pferd)
        if form.is_valid():
            form.save()
            return redirect('edit_pferd_success')
    else:
        form = EditPferdForm()
    return render(request, 'mitgliederbereich/edit_pferd.html', {'form': form})

def edit_pferd_success(request):
    return render(request, 'mitgliederbereich/pferde_management.html')
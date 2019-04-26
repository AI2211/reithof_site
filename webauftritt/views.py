import os

from django.shortcuts import render, get_object_or_404, redirect

from django.core.mail import send_mail
from django.core.mail import BadHeaderError
from django.http import HttpResponse

from .forms import ProfileForm, CreateEintrag, CreateKurs
from .models import Profile, Eintrag, Kurs, Pferd


# import requests

def index(request):
    return render(request, 'webauftritt/ritterstall.html')


# def index(request):
# r = requests.get('http://httpbin.org/status/418')
# print(r.text)
# return render(request, '<pre>' + r.text + '</pre>')

def ueber_uns(request):
    all_profiles = Profile.objects.all()
    context = {'all_profiles': all_profiles}
    return render(request, 'webauftritt/ueber_uns.html', context)


def kurse(request):
    all_kurs = Kurs.objects.all()
    kurs_bool = "false"
    if request.method == "POST":
        form = CreateKurs(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = CreateKurs()
    else:
        form = CreateKurs()
    return render(request, 'webauftritt/kurse.html', {'all_kurs': all_kurs, 'form': form})


def galerie(request):
    path = "webauftritt/static/webauftritt/images"
    dirs = os.listdir(path)

    for file in dirs:
        print(file)
    images_dict = {key: i for i, key in enumerate(dirs)}
    #files = os.listdir(os.path.join(settings.STATIC_ROOT, "webauftritt/images"))
    return render(request, 'webauftritt/galerie.html', {'images_dict': images_dict})


def unsere_pferde(request):
    profile = get_object_or_404(Profile, email="admin@admin.com")
    all_pferde = Pferd.objects.all().filter(besitzer=profile)

    return render(request, 'webauftritt/unsere_pferde.html', {'all_pferde': all_pferde})


def news(request):
    all_eintrag = Eintrag.objects.all()

    if request.method == "POST":
        form = CreateEintrag(request.POST, request.FILES)
        if form.is_valid():
            eintrag = form.save(commit=False)
            eintrag.autor = request.user
            eintrag.save()
    else:
        form = CreateEintrag()
    return render(request, 'webauftritt/news.html', {'form': form, 'all_eintrag': all_eintrag})


def kontakt(request):
    if request.method == "POST":
        vorname = request.POST.get('vorname')
        nachname = request.POST.get('nachname')
        email = request.POST.get('email')
        betreff = request.POST.get('betreff')
        nachricht = request.POST.get('nachricht')
        alles = "%s %s via %s %s: %s" % (
            vorname,
            nachname,
            email,
            betreff,
            nachricht
        )
        try:
            send_mail(betreff,
                      alles,
                      email,
                      ['djangotest255@gmail.com'],
                      fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponse('Vielen Dank für deine Nachricht')
    else:
        return render(request, 'webauftritt/kontakt.html')


def impressum(request):
    return render(request, 'webauftritt/impressum.html')

def datenschutz(request):
    return render(request, 'webauftritt/datenschutz.html')


def register(request):
    if request.method == "POST":
        profile_form = ProfileForm(request.POST or None)
        if profile_form.is_valid():
            user = profile_form.save(commit=False)
            vorname = profile_form.cleaned_data['vorname']
            nachname = profile_form.cleaned_data['nachname']
            email = profile_form.cleaned_data['email']
            # send_mail('Hello from Test', 'Hello I am Test', settings.EMAIL_HOST_USER, [email], fail_silently=False)
            profile_form.save()
            return redirect('login')
    else:
        profile_form = ProfileForm()
    return render(request, 'webauftritt/register.html', {'profile_form': profile_form})


def delete_kurs(request, pk):
    kurs = get_object_or_404(Kurs, pk=pk)
    kurs.delete()

    return render(request, 'webauftritt/deleted_kurs.html', {'kurs': kurs})

def eintragen_kurs(request, pk):
    kurs = get_object_or_404(Kurs, pk=pk)
    request.user.Kurse.add(kurs)
    request.user.save()

    return render(request, 'webauftritt/added_user_kurs.html', {'kurs': kurs})

def austragen_kurs(request, pk):
    kurs = get_object_or_404(Kurs, pk=pk)
    request.user.Kurse.remove(kurs)
    request.user.save()

    return render(request, 'webauftritt/removed_user_kurs.html', {'kurs': kurs})

def delete_news(request, pk):
    eintrag = get_object_or_404(Eintrag, pk=pk)
    eintrag.delete()

    return render(request, 'webauftritt/deleted_news.html', {'eintrag': eintrag})
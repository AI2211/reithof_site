from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.db.models import signals

from .managers import ProfileUserManager


class Kurs(models.Model):
    name = models.CharField(max_length=100)
    beschreibung = models.CharField(max_length=200)
    bild = models.ImageField(blank=True)

    class Meta:
        verbose_name = _('Kurs')
        verbose_name_plural = _('Kurse')

    def __str__(self):
        return self.name


class Profile(AbstractBaseUser, PermissionsMixin):
    Kurse = models.ManyToManyField(Kurs)
    #Username
    username = models.CharField(_('Username'), max_length=150, blank=True)
    #Vorname
    vorname = models.CharField(_('Vorname'), max_length=50, blank=True)
    #Nachname
    nachname = models.CharField(_('Nachname'), max_length=50, blank=True)
    #Passwort
    password = models.CharField(_('Passwort'), max_length=128)
    #Letzte Anmeldung
    last_login = models.DateTimeField(_('Letzte Anmeldung'), blank=True, null=True)
    #Email
    email = models.EmailField(
        _('Email-Adresse'),
        unique=True,
        error_messages={
            'unique': _("Ein Nutzer mit dieser E-Mail-Adresse existiert bereits!"),
        },
    )
    #Geburtsdatum
    geburtsdatum = models.DateField(_('Geburtsdatum'), auto_now_add=False, auto_now=False, null=True, blank=True)
    #Mistpunkte
    mistpunkte = models.IntegerField(null=True, blank=True)
    #Erstellt am
    date_joined = models.DateTimeField(_('Erstellt am'), default=timezone.now)
    #Ist Superuser
    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
        help_text=_(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    #aktiv
    is_active = models.BooleanField(
        _('aktiv'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    objects = ProfileUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['vorname', 'nachname']

    class Meta:
        verbose_name = _('Mitglied')
        verbose_name_plural = _('Mitglieder')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.vorname, self.nachname)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.vorname

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

class Eintrag(models.Model):
    autor = models.ForeignKey(Profile, on_delete=models.CASCADE)
    titel = models.CharField(max_length=250)
    nachricht = models.TextField()
    erstellt_am = models.DateTimeField(_('Erstellt am'), default=timezone.now)
    kategorie = models.CharField(max_length=100)
    bild = models.ImageField(blank=True)

    class Meta:
        verbose_name = _('Eintrag')
        verbose_name_plural = _('Einträge')

    def __str__(self):
        return self.titel

class Kategorie(models.Model):
    name = models.CharField(max_length=100)
    long = models.IntegerField(blank=True)
    lat = models.IntegerField(blank=True)

    class Meta:
        verbose_name =_('Kategorie')
        verbose_name_plural = _('Kategorien')

    def __str__(self):
        return self.name

class Pferdegruppe(models.Model):
    name = models.CharField(max_length=100)
    long = models.IntegerField(blank=True)
    lat = models.IntegerField(blank=True)

    class Meta:
        verbose_name = _('Pferdegruppe')
        verbose_name_plural = _('Pferdegruppen')

    def __str__(self):
        return self.name

class Pferd(models.Model):
    besitzer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pferdgruppe = models.ForeignKey(Pferdegruppe, on_delete=models.CASCADE, blank=True)
    offizieller_name = models.CharField(max_length=100)
    rufname = models.CharField(max_length=100)
    geburtstag = models.DateTimeField(blank=True)
    kategorie = models.ForeignKey(Kategorie, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Pferd')
        verbose_name_plural = _('Pferde')

    def __str__(self):
        return self.offizieller_name





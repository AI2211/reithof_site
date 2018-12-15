from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from .managers import ProfileUserManager

class Eintrag(models.Model):
    titel = models.CharField(max_length=250)
    nachricht = models.TextField()
    erstellt_am = models.DateTimeField(_('Erstellt am'), default=timezone.now)

    class Meta:
        verbose_name = _('Eintrag')
        verbose_name_plural = _('Einträge')


class Pferd(models.Model):
    offizieller_name = models.CharField(max_length=100)
    rufname = models.CharField(max_length=100)
    geburtstag = models.DateTimeField(blank=True)
    kategorie = models.CharField(max_length=100)

    class Meta:
        verbose_name = _('Pferd')
        verbose_name_plural = _('Pferde')


class Profile(AbstractBaseUser, PermissionsMixin):
    #Pferd
    pferd = models.ForeignKey(Pferd, on_delete=models.CASCADE, blank=True, null=True)
    #Einträge
    eintrag = models.ForeignKey(Eintrag, on_delete=models.CASCADE, blank=True, null=True)
    #Username
    username = models.CharField(_('Username'), max_length=150)
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
    geburtsdatum = models.DateField(_('Geburtsdatum'), auto_now_add=False, auto_now=False, null=True)
    #Mistpunkte
    mistpunkte = models.IntegerField(null=True)
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
        default=True,
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

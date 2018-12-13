from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class ProfileUserManager(BaseUserManager):
    def create_user(self, vorname, nachname, email, passwort, alias=None):
        if not vorname:
            raise ValueError("Vorname muss eingetragen sein!")
        if not nachname:
            raise ValueError("Nachname muss eingetragen sein!")
        if not email:
            raise ValueError("Eine E-Mail-Adresse muss eingetragen sein!")
        if not passwort:
            raise ValueError("Bitte Passwort eingeben!")
        if not alias:
            alias = vorname

        user = self.model(
            email=self.normalize_email(email),
            vorname=vorname,
            nachname=nachname,
            alias=alias)
        user.set_password(passwort)
        user.save()
        return user

    def create_superuser(self, vorname, nachname, email, passwort, alias=None):
        user = self.create_user(email, vorname, nachname, passwort, alias)
        user.is_staff()
        user.is_superuser = True
        user.save()
        return user



class Pferd(models.Model):
    offizieller_name = models.CharField(max_length=100)
    rufname = models.CharField(max_length=100)
    geburtstag = models.DateTimeField(blank=True)
    kategorie = models.CharField(max_length=100)


class Profile(AbstractBaseUser, PermissionsMixin):
    vorname = models.CharField(_('Vorname'), max_length=50, blank=True)
    nachname = models.CharField(_('Nachname'), max_length=50, blank=True)
    email = models.EmailField(_('Email-Adresse'), unique=True)
    erstellt_am = models.DateTimeField(_('Erstellt am'), auto_now_add=True)
    geburtsdatum = models.DateField(_('Geburtsdatum'), auto_now_add=False, auto_now=False)
    mistpunkte = models.IntegerField(null=True)

    objects = ProfileUserManager

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









    #pferd = models.ForeignKey(Pferd, on_delete=models.CASCADE)
    #vorname = models.CharField(max_length=100)
    #nachname = models.CharField(max_length=100)
    #email = models.CharField(max_length=100)
    #password = models.CharField(max_length=100)
    #erstellt_am = models.DateField(auto_now_add=True)
    #ist_aktiv = models.BooleanField(default=False)


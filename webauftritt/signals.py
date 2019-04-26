from django.db.models.signals import pre_save, post_save
from django.core.mail import send_mail
from django.dispatch import receiver

from reithof_site import settings
from .models import Profile


# Versendet eine Email an den Nutzer wenn er aktiv geschalten wurde
@receiver(pre_save, sender=Profile, dispatch_uid='active')
def active(sender, instance, **kwargs):
    if instance.is_active and Profile.objects.filter(pk=instance.pk, is_active=False).exists():
        subject = 'Accountaktivierung'
        mesagge = '%s dein Account ist nun aktiv' % (instance.email)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, mesagge, from_email, [instance.email], fail_silently=False)


# Versendet eine Email an den Admin bei Erstellung eines neuen Accounts
@receiver(post_save, sender=Profile, dispatch_uid='register')
def register(sender, instance, **kwargs):
    if kwargs.get('created', False):
        subject = 'Neuer Account: %s' % (instance.email)
        mesagge = 'Neuer Account mit der Email %s wurde angelegt' % (instance.email)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, mesagge, from_email, [from_email], fail_silently=False)

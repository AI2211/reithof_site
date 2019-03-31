from django import forms
from .models import Eintrag, Kurs
from django.contrib.auth.forms import get_user_model, authenticate, password_validation
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.conf import settings
#from .admin import ProfileCreationForm

class ProfileForm(UserCreationForm):
    error_messages = {
        'password_mismatch': _("Passwörter sind nicht gleich"),
    }

    password1 = forms.CharField(
        label=_("Passwort"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Passwort bestätigen"),
        widget=forms.PasswordInput,
        strip=False,
    )


    class Meta:
        model = get_user_model()
        fields = ['email', 'vorname', 'nachname', 'password1', 'password2']

class CreateEintrag(forms.ModelForm):
    class Meta:
        model = Eintrag
        fields = ['titel', 'nachricht', 'kategorie', 'bild']

class CreateKurs(forms.ModelForm):
    class Meta:
        model = Kurs
        fields = '__all__'

class ProfileChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'
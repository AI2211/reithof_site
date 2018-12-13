from django import forms
from .models import Profile
from django.contrib.auth.forms import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
#from .admin import ProfileCreationForm

# class UserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(label='Passwort', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Passwort bestätigen', widget=forms.PasswordInput)
#
#     class Meta:
#         model = get_user_model()
#         fields = ['vorname', 'nachname', 'email', 'geburtsdatum']
#
#     def clean_password(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwörter stimmen nicht überein!")
#         return password2
#
#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return user

class ProfileForm(UserCreationForm):


    class Meta:
        model = get_user_model()
        fields = '__all__'

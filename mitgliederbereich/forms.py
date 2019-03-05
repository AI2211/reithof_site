from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import get_user_model

class EmailChangeForm(forms.Form):

    error_messages = {
        'email_mismatch': _("Die E-Mail-Adresse stimmen nicht überein!"),
        'not_changed': _("Es wird die selbe E-Mail-Adresse genutzt!"),
    }

    new_email1 = forms.EmailField(
        label=_("Neue E-Mail-Adresse"),
        widget=forms.EmailInput,
    )

    new_email2 = forms.EmailField(
        label=_("Neue E-Mail-Adresse bestätigen"),
        widget=forms.EmailInput,
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(EmailChangeForm, self).__init__(*args, **kwargs)

    def clean_new_email1(self):
        old_email = self.user.email
        new_email1 = self.cleaned_data.get('new_email1')
        if new_email1 and old_email:
            if new_email1 == old_email:
                raise forms.ValidationError(
                    self.error_messages['not_changed'],
                    code='not_changed',
                )
        return new_email1

    def clean_new_email2(self):
        new_email1 = self.cleaned_data.get('new_email1')
        new_email2 = self.cleaned_data.get('new_email2')
        if new_email1 and new_email2:
            if new_email1 != new_email2:
                raise forms.ValidationError(
                    self.error_messages['email_mismatch'],
                    code='email_mismatch',
                )
        return new_email2

    def save(self, commit=True):
        email = self.cleaned_data["new_email1"]
        self.user.email = email
        if commit:
            self.user.save()
        return self.user
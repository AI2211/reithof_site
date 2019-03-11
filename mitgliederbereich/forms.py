from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm, DateInput
from mitgliederbereich.models import Event


class EmailChangeForm(forms.Form):
    error_messages = {
        'password_incorrect': _("Das Passwort ist nicht korrekt!"),
        'email_mismatch': _("Die E-Mail-Adresse stimmen nicht überein!"),
        'not_changed': _("Es wird die selbe E-Mail-Adresse genutzt!"),
    }

    password = forms.CharField(
        label=_("Passwort"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autofocus': True}),
    )

    new_email1 = forms.EmailField(
        label=_("Neue E-Mail-Adresse"),
        widget=forms.EmailInput,
    )

    new_email2 = forms.EmailField(
        label=_("Neue E-Mail-Adresse bestätigen"),
        widget=forms.EmailInput,
    )

    field_order = ['password', 'new_email1', 'new_email2']

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

    def clean_password(self):
        """
        Validate that the old_password field is correct.
        """
        password = self.cleaned_data["password"]
        if not self.user.check_password(password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return password

    def save(self, commit=True):
        email = self.cleaned_data["new_email1"]
        self.user.email = email

        if commit:
            self.user.save()
        return self.user


class EventForm(ModelForm):
    class Meta:
        model = Event
        # datetime-local is a HTML5 input type, format to make date time show on fields
        widgets = {
            'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats parses HTML5 datetime-local input to datetime field
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)



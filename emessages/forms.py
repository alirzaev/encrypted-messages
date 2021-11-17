from django import forms
from django.contrib.auth.password_validation import validate_password


class CreateEncryptedMessageForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, validators=[validate_password])

    message = forms.CharField(widget=forms.Textarea, max_length=2000)


class DecryptEncryptedMessageForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, validators=[validate_password])

from django import forms

from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        fields = ["name", "phone", "email", "activity"]
        model = Client

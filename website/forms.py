from django import forms

from .models import Client
from django.utils.safestring import mark_safe
from django.urls import reverse_lazy


class ClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        link = reverse_lazy("privacy_policy")
        self.fields["consent"].label = mark_safe(
            f"Wyrażam zgodę na przetwarzanie moich danych osobowych zgodnie z <a href='{link}'>Polityką prywatności</a>"
        )
        self.fields["consent"].label_suffix = ""

    class Meta:
        fields = ["name", "phone", "email", "activity", "consent"]
        model = Client

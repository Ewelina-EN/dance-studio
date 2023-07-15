from django import forms

from .models import Client
from django.utils.safestring import mark_safe


class ClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields["consent"].label = mark_safe(
            "Wyrażam zgodę na przetwarzanie moich danych osobowych zgodnie z <a href=''>Polityką prywatności</a>"
        )

    class Meta:
        fields = ["name", "phone", "email", "activity", "consent"]
        model = Client

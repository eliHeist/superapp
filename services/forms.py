from services.models import Service
from django.forms import ModelForm


class ServiceModelForm(ModelForm):
    class Meta:
        model = Service
        fields = (
            'name',
            'description'
        )
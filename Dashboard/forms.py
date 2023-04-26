from django import forms
from .models import Dashboard

class DashForm(forms.ModelForm):
    class Meta:
        model = Dashboard

        fields = {
            "title",
            "description",
        }

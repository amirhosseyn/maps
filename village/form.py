from django.forms import ModelForm
from django import forms
from .models import Village


class VillageForm(ModelForm):
    class Meta:
        model = Village
        fields = '__all__'


class SearchForm(forms.Form):
    search = forms.CharField(label='Search', max_length=100)
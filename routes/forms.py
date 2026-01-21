from django import forms
from .models import AirportRoute

class AirportRouteForm(forms.ModelForm):
    class Meta:
        model=AirportRoute
        fields=['airport_code','parent','position','duration']

class NthNodeSearchForm(forms.Form):
    root_airport=forms.ModelChoiceField(
        queryset=AirportRoute.objects.all(),
        label="Start from Airport (Root/Parent)")
    
    n=forms.IntegerField(label="Nth Node",min_value=1)
    position=forms.ChoiceField(choices=[('left','Left'),('right','Right')])


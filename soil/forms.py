from django import forms
from .models import upload_soil_data_class

class soil_data_form(forms.ModelForm):
    class Meta:
        model =  upload_soil_data_class
        fields = ['N', 'P', 'K', 'Temperature', 'Humidity', 'Ph', 'Rainfall']


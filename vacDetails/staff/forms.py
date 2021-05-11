from django import forms
#from django.forms import ImageField
from .models import vaccineDetails 
from django.contrib import messages
import datetime
from django.contrib.admin import widgets

class VacForm(forms.ModelForm):
    class Meta:
        model = vaccineDetails
        fields = [
            'staff_name',
            'staff_no',
            'dp_code',
            'branch_name',
            'ro_code',
            'circle_name',
            'vaccinated',
            'vaccinated_date',
            'contact_number',
        ]
    vaccinated_date = forms.DateTimeField( initial=datetime.datetime.now)
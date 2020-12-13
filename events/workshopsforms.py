from django import forms
from .models import *

class StandUpWorkshopForm(forms.ModelForm):
    event_name = "standupworkshop"
    class Meta:
        model = StandUpWorkshop
        fields = ['name','age','phoneNum','college','email']

        labels = {
        "name": "",
        "phoneNum": "",
        'college':'',
        'email':'',
        'age':'',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Contact Number'}),
            'college': forms.TextInput(attrs={'placeholder': 'College Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Id'}),
            'age':forms.NumberInput(attrs={'placeholder':'Age'}),
        }


class InfluentialTrendsWorkshopForm(forms.ModelForm):
    event_name = "influentialtrends"
    class Meta:
        model = InfluentialTrendsWorkshop
        fields = ['name','age','phoneNum','college','email']

        labels = {
        "name": "",
        "phoneNum": "",
        'college':'',
        'email':'',
        'age':'',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Contact Number'}),
            'college': forms.TextInput(attrs={'placeholder': 'College Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Id'}),
            'age':forms.NumberInput(attrs={'placeholder':'Age'}),
        }

class DanceWorkshopForm(forms.ModelForm):
    event_name = "danceworkshop"
    class Meta:
        model = DanceWorkshop
        fields = ['name','age','phoneNum','college','email']

        labels = {
        "name": "",
        "phoneNum": "",
        'college':'',
        'email':'',
        'age':'',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Contact Number'}),
            'college': forms.TextInput(attrs={'placeholder': 'College Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Id'}),
            'age':forms.NumberInput(attrs={'placeholder':'Age'}),
        }

class FitnessWorkshopForm(forms.ModelForm):
    event_name = "fitnessworkshop"
    class Meta:
        model = FitnessWorkshop
        fields = ['name','age','phoneNum','college','email']

        labels = {
        "name": "",
        "phoneNum": "",
        'college':'',
        'email':'',
        'age':'',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Contact Number'}),
            'college': forms.TextInput(attrs={'placeholder': 'College Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Id'}),
            'age':forms.NumberInput(attrs={'placeholder':'Age'}),
        }

class ActingWorkshopForm(forms.ModelForm):
    event_name = "actingworkshop"
    class Meta:
        model = ActingWorkshop
        fields = ['name','age','phoneNum','college','email']

        labels = {
        "name": "",
        "phoneNum": "",
        'college':'',
        'email':'',
        'age':'',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Contact Number'}),
            'college': forms.TextInput(attrs={'placeholder': 'College Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Id'}),
            'age':forms.NumberInput(attrs={'placeholder':'Age'}),
        }

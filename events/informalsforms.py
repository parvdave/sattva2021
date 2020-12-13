from django import forms
from .models import *

class PopCultureForm(forms.ModelForm):
    event_name = "popculture"
    class Meta:
        model = PopCulture
        fields = ['name1','phoneNum1','college1','city1','gender1','name2','phoneNum2','college2','city2','gender2']
        labels = {
            'name1': "",
            'phoneNum1': "",
            'college1': "",
            'city1': "",
            'gender1': "Gender of Participant 1",
            'talent1': "",
            'name2': "",
            'phoneNum2': "",
            'college2': "",
            'city2': "",
            'gender2': "Gender of Participant 2",
            'talent2': "",
        }
        widgets = {
            'name1': forms.TextInput(attrs={'placeholder': 'Name of Participant 1'}),
            'phoneNum1': forms.TextInput(attrs={'placeholder': 'Contact number of Participant 1'}),
            'college1': forms.TextInput(attrs={'placeholder': 'Name of College 1'}),
            'city1': forms.TextInput(attrs={'placeholder': 'City of Residence (Participant 1)'}),
            'gender1': forms.RadioSelect(attrs={}),
            'name2': forms.TextInput(attrs={'placeholder': 'Name of Participant 1'}),
            'phoneNum2': forms.TextInput(attrs={'placeholder': 'Contact number of Participant 2'}),
            'college2': forms.TextInput(attrs={'placeholder': 'Name of College 2'}),
            'city2': forms.TextInput(attrs={'placeholder': 'City of Residence (Participant 2)'}),
            'gender2': forms.RadioSelect(attrs={}),
        }

class MrMsSattvaForm(forms.ModelForm):
    event_name = "mrmssattva"
    class Meta:
        model = MrMsSattva
        fields = ['name','phoneNum','college','city','gender','talent']
        labels = {
            'name': "",
            'phoneNum': "",
            'college': "",
            'city': "",
            'gender': "Gender of Participant 1",
            'talent':"",
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name of Participant 1'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Contact number of Participant 1'}),
            'college': forms.TextInput(attrs={'placeholder': 'Name of College 1'}),
            'city': forms.TextInput(attrs={'placeholder': 'City of Residence (Participant 1)'}),
            'gender': forms.RadioSelect(attrs={}),
            'talent': forms.TextInput(attrs={'placeholder':'Talents (eg. Singing, dancing)'}),
        }

class PunIntendedForm(forms.ModelForm):
    event_name = "punintended"
    class Meta:
        model = PunIntended
        fields = ['name','phoneNum','college','city','gender']
        labels = {
            'name': "",
            'phoneNum': "",
            'college': "",
            'city': "",
            'gender': "Gender of Participant 1"
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name of Participant 1'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Contact number of Participant 1'}),
            'college': forms.TextInput(attrs={'placeholder': 'Name of College 1'}),
            'city': forms.TextInput(attrs={'placeholder': 'City of Residence (Participant 1)'}),
            'gender': forms.RadioSelect(attrs={}),
        }


from django import forms
from .models import *

class PhotographyForm(forms.ModelForm):
    event_name = "photography"
    class Meta:
        model = Photography
        fields = ['name','phoneNum','email', 'whatsapp', 'type1', 'type2']

        labels = {
        "name": "",
        "phoneNum": "",
        'email':'',
        'whatsapp':'',
        'type1' : 'Interested In Photography Contest',
        'type2' : 'Interested In Videography Contest'
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Contact Number'}),
            'college': forms.TextInput(attrs={'placeholder': 'College'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email ID'}),
            'whatsapp': forms.TextInput(attrs={'placeholder': 'WhatsApp Number'})
        }
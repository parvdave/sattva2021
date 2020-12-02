from django import forms
from .models import SoloSinging

class SoloSingingForm(forms.ModelForm):
    class Meta:
        model = SoloSinging
        fields = ['name','email','phoneNum','college']
        labels = {
        "name": "Enter your name: ",
        "email": "Enter your email: ",
        'phoneNum':"Enter your contact number: ",
        'college':"Enter college: ",
        }
from django import forms
from .models import SoloSinging,GroupEventPA,Poetry

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

class GroupSingingForm(forms.ModelForm):
    event_name = "groupsinging"
    class Meta:
        model = GroupEventPA
        fields = ['name','email','phoneNum','college','groupname']
        labels = {
        "name": "Enter your name: ",
        "email": "Enter your email: ",
        'phoneNum':"Enter your contact number: ",
        'college':"Enter college: ",
        'groupname':"Enter name of your group",
        }

class PoetryForm(forms.ModelForm):
    event_name = "poetry"
    class Meta:
        model = Poetry
        fields = ['name','age','email','address','phoneNum','whatsapp','contacted']
        labels = {
        "name": "Enter your name: ",
        "email": "Enter your email: ",
        'age':'Enter age: ',
        'address':'Enter your address: ',
        'phoneNum':"Enter your contact number: ",
        'whatsapp':"Enter your whatsapp number: ",
        'contacted':"Have you already received the details regarding the first phase of the competition (By someone from our team)? (Yes/No) ",
        }
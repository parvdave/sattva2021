from django import forms
from .models import SoloSinging,GroupEventPA

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
    event_name = "group_singing"
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
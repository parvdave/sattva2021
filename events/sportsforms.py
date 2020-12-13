from django import forms
from .models import Fifa,RocketLeague,PUBG

class FifaForm(forms.ModelForm):
    event_name = "fifa"
    class Meta:
        model = Fifa
        fields = ['name','phoneNum']

        labels = {
        "name": "",
        "phoneNum": ""
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Contact Number'}),
        }

class RocketLeagueForm(forms.ModelForm):
    event_name = "rocketleague"
    class Meta:
        model = RocketLeague
        fields = ['name1','phoneNum1','rank1', 'name2','phoneNum2','rank2', 'name3','phoneNum3','rank3']
        labels = {
        "name1": "",
        "phoneNum1": "",
        'rank1':'',
        "name2": "",
        "phoneNum2": "",
        'rank2':'',
        "name3": "",
        "phoneNum3": "",
        'rank3':'',
        }

        widgets = {
            'name1': forms.TextInput(attrs={'placeholder': 'Name'}),
            'phoneNum1': forms.TextInput(attrs={'placeholder': 'Contact Number'}),
            'rank1': forms.TextInput(attrs={'placeholder': 'Your Rank'}),
            'name2': forms.TextInput(attrs={'placeholder': 'Name of 2nd Participant'}),
            'phoneNum2': forms.TextInput(attrs={'placeholder': 'Contact Number of 2nd Participant'}),
            'rank2': forms.TextInput(attrs={'placeholder': 'Rank of 2nd Participant'}),
            'name3': forms.TextInput(attrs={'placeholder': 'Name of 3rd Participant'}),
            'phoneNum3': forms.TextInput(attrs={'placeholder': 'Contact Number of 3rd Participant'}),
            'rank3': forms.TextInput(attrs={'placeholder': 'Rank of 3rd Participant'}),
        }

class PUBGForm(forms.ModelForm):
    event_name = "pubg"
    class Meta:
        model = PUBG
        fields = ['name1','phoneNum1','tier1', 'name2','phoneNum2','tier2', 'name3','phoneNum3','tier3', 'name4','phoneNum4','tier4']
        labels = {
        "name1": "",
        "phoneNum1": "",
        'tier1':'',
        "name2": "",
        "phoneNum2": "",
        'tier2':'',
        "name3": "",
        "phoneNum3": "",
        'tier3':'',
        "name4": "",
        "phoneNum4": "",
        'tier4':'',
        }

        widgets = {
            'name1': forms.TextInput(attrs={'placeholder': 'Name'}),
            'phoneNum1': forms.TextInput(attrs={'placeholder': 'Contact Number'}),
            'tier1': forms.TextInput(attrs={'placeholder': 'Your Tier'}),
            'name2': forms.TextInput(attrs={'placeholder': 'Name of 2nd Participant'}),
            'phoneNum2': forms.TextInput(attrs={'placeholder': 'Contact Number of 2nd Participant'}),
            'tier2': forms.TextInput(attrs={'placeholder': 'Tier of 2nd Participant'}),
            'name3': forms.TextInput(attrs={'placeholder': 'Name of 3rd Participant'}),
            'phoneNum3': forms.TextInput(attrs={'placeholder': 'Contact Number of 3rd Participant'}),
            'tier3': forms.TextInput(attrs={'placeholder': 'Tier of 3rd Participant'}),
            'name4': forms.TextInput(attrs={'placeholder': 'Name of 4th Participant'}),
            'phoneNum4': forms.TextInput(attrs={'placeholder': 'Contact Number of 4th Participant'}),
            'tier4': forms.TextInput(attrs={'placeholder': 'Tier of 4th Participant'}),
        }
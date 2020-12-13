from django import forms
from .models import AdVision, Turnaround, Bidweiser, TazhaKhabar, HouseOfBattle, MarketGuru

class AdVisionForm(forms.ModelForm):
    event_name = "advision"
    class Meta:
        model = AdVision
        fields = ['name1','phoneNum1','college1','email1','name2','phoneNum2','college2','email2', 'name3','phoneNum3','college3','email3']

        labels = {
        "name1": "",
        "phoneNum1": "",
        'college1':'',
        'email1':'',
        "name2": "",
        "phoneNum2": "",
        'college2':'',
        'email2':'',
        "name3": "",
        "phoneNum3": "",
        'college3':'',
        'email3':'',
        }

        widgets = {
            'name1': forms.TextInput(attrs={'placeholder': 'Name'}),
            'phoneNum1': forms.TextInput(attrs={'placeholder': 'Contact Number'}),
            'college1': forms.TextInput(attrs={'placeholder': 'College Name'}),
            'email1': forms.EmailInput(attrs={'placeholder': 'Email Id'}),
            'name2': forms.TextInput(attrs={'placeholder': 'Name of 2nd Participant'}),
            'phoneNum2': forms.TextInput(attrs={'placeholder': 'Contact Number of 2nd Participant'}),
            'college2': forms.TextInput(attrs={'placeholder': 'College Name of 2nd Participant'}),
            'email2': forms.EmailInput(attrs={'placeholder': 'Email Id of 2nd Participant'}),
            'name3': forms.TextInput(attrs={'placeholder': 'Name of 3rd Participant'}),
            'phoneNum3': forms.TextInput(attrs={'placeholder': 'Contact Number of 3rd Participant'}),
            'college3': forms.TextInput(attrs={'placeholder': 'College Name of 3rd Participant'}),
            'email3': forms.EmailInput(attrs={'placeholder': 'Email Id of 3rd Participant'}),
        }

class TurnaroundForm(forms.ModelForm):
    event_name = "turnaround"
    class Meta:
        model = Turnaround
        fields = ['name','phoneNum','college','email']

        labels = {
        "name": "",
        "phoneNum": "",
        'college':'',
        'email':'',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Contact Number'}),
            'college': forms.TextInput(attrs={'placeholder': 'College Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Id'}),
        }

class BidweiserForm(forms.ModelForm):
    event_name = "bidweiser"
    class Meta:
        model = Bidweiser
        fields = ['name1','phoneNum1','college1','email1', 'name2','phoneNum2','college2','email2']
        labels = {
        "name1": "",
        "phoneNum1": "",
        'college1':'',
        'email1':'',
        "name2": "",
        "phoneNum2": "",
        'college2':'',
        'email2':'',
        }

        widgets = {
            'name1': forms.TextInput(attrs={'placeholder': 'Name'}),
            'phoneNum1': forms.TextInput(attrs={'placeholder': 'Contact Number'}),
            'college1': forms.TextInput(attrs={'placeholder': 'College Name'}),
            'email1': forms.EmailInput(attrs={'placeholder': 'Email Id'}),
            'name2': forms.TextInput(attrs={'placeholder': 'Name of 2nd Participant'}),
            'phoneNum2': forms.TextInput(attrs={'placeholder': 'Contact Number of 2nd Participant'}),
            'college2': forms.TextInput(attrs={'placeholder': 'College Name of 2nd Participant'}),
            'email2': forms.EmailInput(attrs={'placeholder': 'Email Id of 2nd Participant'}),
        }

class TazhaKhabarForm(forms.ModelForm):
    event_name = "tazhakhabar"
    class Meta:
        model = TazhaKhabar
        fields = ['name','phoneNum','college','email', 'day']

        labels = {
        "name": "",
        "phoneNum": "",
        'college':'',
        'email':'',
        'day' : 'Choose Your Day Of Participation'
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Contact Number'}),
            'college': forms.TextInput(attrs={'placeholder': 'College Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Id'}),
            'day': forms.RadioSelect(attrs={}),
        }

class HouseOfBattleForm(forms.ModelForm):
    event_name = "houseofbattle"
    class Meta:
        model = HouseOfBattle
        fields = ['name1','phoneNum1','college1','email1', 'name2','phoneNum2','college2','email2']
        labels = {
        "name1": "",
        "phoneNum1": "",
        'college1':'',
        'email1':'',
        "name2": "",
        "phoneNum2": "",
        'college2':'',
        'email2':'',
        }

        widgets = {
            'name1': forms.TextInput(attrs={'placeholder': 'Name'}),
            'phoneNum1': forms.TextInput(attrs={'placeholder': 'Contact Number'}),
            'college1': forms.TextInput(attrs={'placeholder': 'College Name'}),
            'email1': forms.EmailInput(attrs={'placeholder': 'Email Id'}),
            'name2': forms.TextInput(attrs={'placeholder': 'Name of 2nd Participant'}),
            'phoneNum2': forms.TextInput(attrs={'placeholder': 'Contact Number of 2nd Participant'}),
            'college2': forms.TextInput(attrs={'placeholder': 'College Name of 2nd Participant'}),
            'email2': forms.EmailInput(attrs={'placeholder': 'Email Id of 2nd Participant'}),
        }

class MarketGuruForm(forms.ModelForm):
    event_name = "marketguru"
    class Meta:
        model = MarketGuru
        fields = ['name','phoneNum','college','email']

        labels = {
        "name": "",
        "phoneNum": "",
        'college':'',
        'email':'',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Contact Number'}),
            'college': forms.TextInput(attrs={'placeholder': 'College Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Id'}),
        }
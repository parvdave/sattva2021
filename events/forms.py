from django import forms
from .models import *

class SoloSingingForm(forms.ModelForm):
    event_name = "solosinging"
    class Meta:
        model = SoloSinging
        fields = ['name','age','email','country','address','phoneNum','whatsapp','contacted']
        labels = {
        "name": "",
        "email": "",
        'age':'',
        'address':'',
        'phoneNum':"",
        'whatsapp':"",
        'country':'',
        'contacted':"Have you already received the details regarding the first phase of the competition (By someone from our team)? (Yes/No) ",
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email':forms.EmailInput(attrs={'placeholder': 'Email'}),
            'age':forms.NumberInput(attrs={'placeholder':'Age'}),
            'address':forms.Textarea(attrs={'placeholder':'Address'}),
            'phoneNum':forms.TextInput(attrs={'placeholder':"Contact Number"}),
            'whatsapp':forms.TextInput(attrs={'placeholder':"Whatsapp Number"}),
            'country':forms.TextInput(attrs={'placeholder':'Country'}),
        }

class GroupSingingForm(forms.ModelForm):
    event_name = "groupsinging"
    class Meta:
        model = GroupSinging
        fields = ['name','age','email','country','address','phoneNum','whatsapp','contacted']
        labels = {
        "name": "Enter your name: ",
        "email": "Enter your email: ",
        'age':'Enter age: ',
        'address':'Enter your address: ',
        'phoneNum':"Enter your contact number: ",
        'whatsapp':"Enter your whatsapp number: ",
        'contacted':"Have you already received the details regarding the first phase of the competition (By someone from our team)? (Yes/No) ",
        }

class PoetryForm(forms.ModelForm):
    event_name = "poetry"
    class Meta:
        model = Poetry
        fields = ['name','age','email','country','address','phoneNum','whatsapp','contacted']
        labels = {
        "name": "",
        "email": "",
        'age':'',
        'address':'',
        'phoneNum':"",
        'whatsapp':"",
        'country':'',
        'contacted':"Have you already received the details regarding the first phase of the competition (By someone from our team)? (Yes/No) ",
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email':forms.EmailInput(attrs={'placeholder': 'Email'}),
            'age':forms.NumberInput(attrs={'placeholder':'Age'}),
            'address':forms.Textarea(attrs={'placeholder':'Address'}),
            'phoneNum':forms.TextInput(attrs={'placeholder':"Contact Number"}),
            'whatsapp':forms.TextInput(attrs={'placeholder':"Whatsapp Number"}),
            'country':forms.TextInput(attrs={'placeholder':'Country'}),
        }

class ShortFilmsForm(forms.ModelForm):
    event_name = "shortfilms"
    class Meta:
        model = ShortFilms
        fields = ['name','nameoffilm','genreoffilm','email','address','country','phoneNum','whatsapp','contacted']
        labels = {
        "name": "",
        "nameoffilm": "",
        'genreoffilm':'',
        'address':'',
        'email':"",
        'phoneNum':"",
        'whatsapp':"",
        'country':'',
        'contacted':"Have you already received the details regarding the first phase of the competition (By someone from our team)? (Yes/No) ",
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name of head'}),
            'nameoffilm': forms.TextInput(attrs={'placeholder': 'Name of film'}),
            'genreoffilm':forms.TextInput(attrs={'placeholder': 'Genre of film'}),
            'email':forms.EmailInput(attrs={'placeholder': 'Email'}),
            'age':forms.NumberInput(attrs={'placeholder':'Age'}),
            'address':forms.Textarea(attrs={'placeholder':'Address'}),
            'phoneNum':forms.TextInput(attrs={'placeholder':"Contact Number"}),
            'whatsapp':forms.TextInput(attrs={'placeholder':"Whatsapp Number"}),
            'country':forms.TextInput(attrs={'placeholder':'Country'}),
        }

class BeatBoxingForm(forms.ModelForm):
    event_name = "beatboxing"
    class Meta:
        model = BeatBoxing
        fields = ['name','age','email','country','address','phoneNum','whatsapp','contacted']
        labels = {
        "name": "",
        "email": "",
        'age':'',
        'address':'',
        'phoneNum':"",
        'whatsapp':"",
        'country':'',
        'contacted':"Have you already received the details regarding the first phase of the competition (By someone from our team)? (Yes/No) ",
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email':forms.EmailInput(attrs={'placeholder': 'Email'}),
            'age':forms.NumberInput(attrs={'placeholder':'Age'}),
            'address':forms.Textarea(attrs={'placeholder':'Address'}),
            'country':forms.TextInput(attrs={'placeholder':'Country'}),
            'phoneNum':forms.TextInput(attrs={'placeholder':"Contact Number"}),
            'whatsapp':forms.TextInput(attrs={'placeholder':"Whatsapp Number"}),
        }

class MonoActForm(forms.ModelForm):
    event_name = "monoact"
    class Meta:
        model = MonoAct
        fields = ['name','age','email','country','address','phoneNum','whatsapp','contacted']
        labels = {
        "name": "",
        "email": "",
        'age':'',
        'address':'',
        'phoneNum':"",
        'whatsapp':"",
        'country':'',
        'contacted':"Have you already received the details regarding the first phase of the competition (By someone from our team)? (Yes/No) ",
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email':forms.EmailInput(attrs={'placeholder': 'Email'}),
            'age':forms.NumberInput(attrs={'placeholder':'Age'}),
            'address':forms.Textarea(attrs={'placeholder':'Address'}),
            'country':forms.TextInput(attrs={'placeholder':'Country'}),
            'phoneNum':forms.TextInput(attrs={'placeholder':"Contact Number"}),
            'whatsapp':forms.TextInput(attrs={'placeholder':"Whatsapp Number"}),
        }

class RapBattleForm(forms.ModelForm):
    event_name = "rapbattle"
    class Meta:
        model = RapBattle
        fields = ['name','age','email','country','address','phoneNum','whatsapp','contacted']
        labels = {
        "name": "",
        "email": "",
        'age':'',
        'address':'',
        'phoneNum':"",
        'whatsapp':"",
        'country':'',
        'contacted':"Have you already received the details regarding the first phase of the competition (By someone from our team)? (Yes/No) ",
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email':forms.EmailInput(attrs={'placeholder': 'Email'}),
            'age':forms.NumberInput(attrs={'placeholder':'Age'}),
            'address':forms.Textarea(attrs={'placeholder':'Address'}),
            'country':forms.TextInput(attrs={'placeholder':'Country'}),
            'phoneNum':forms.TextInput(attrs={'placeholder':"Contact Number"}),
            'whatsapp':forms.TextInput(attrs={'placeholder':"Whatsapp Number"}),
        }

class ClassicalDanceForm(forms.ModelForm):
    event_name = "classicaldance"
    class Meta:
        model = ClassicalDance
        fields = ['name','age','email','country','address','style','phoneNum','whatsapp','contacted']
        labels = {
        "name": "",
        "email": "",
        'age':'',
        'address':'',
        'phoneNum':"",
        'whatsapp':"",
        'style':"",
        'contacted':"Have you already received the details regarding the first phase of the competition (By someone from our team)? (Yes/No) ",
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email':forms.EmailInput(attrs={'placeholder': 'Email'}),
            'age':forms.NumberInput(attrs={'placeholder':'Age'}),
            'address':forms.Textarea(attrs={'placeholder':'Address'}),
            'country':forms.TextInput(attrs={'placeholder':'Country'}),
            'style':forms.TextInput(attrs={'placeholder':'Style of Dance'}),
            'phoneNum':forms.TextInput(attrs={'placeholder':"Contact Number"}),
            'whatsapp':forms.TextInput(attrs={'placeholder':"Whatsapp Number"}),
        }

class WesternDanceForm(forms.ModelForm):
    event_name = "westerndance"
    class Meta:
        model = WesternDance
        fields = ['name','age','email','country','address','style','phoneNum','whatsapp','contacted']
        labels = {
        "name": "",
        "email": "",
        'age':'',
        'address':'',
        'phoneNum':"",
        'style':"",
        'whatsapp':"",
        'country':"",
        'contacted':"Have you already received the details regarding the first phase of the competition (By someone from our team)? (Yes/No) ",
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email':forms.EmailInput(attrs={'placeholder': 'Email'}),
            'age':forms.NumberInput(attrs={'placeholder':'Age'}),
            'address':forms.Textarea(attrs={'placeholder':'Address'}),
            'country':forms.TextInput(attrs={'placeholder':'Country'}),
            'style':forms.TextInput(attrs={'placeholder':'Style of Dance'}),
            'phoneNum':forms.TextInput(attrs={'placeholder':"Contact Number"}),
            'whatsapp':forms.TextInput(attrs={'placeholder':"Whatsapp Number"}),
        }

# Photography

class PhotographyForm(forms.ModelForm):
    event_name = "photographycontest"
    class Meta:
        model = Photography
        fields = ['name','phoneNum','email', 'whatsapp', 'photo', 'video']

        labels = {
        "name": "",
        "phoneNum": "",
        'email':'',
        'whatsapp':'',
        'photo' : 'Interested In Photography Contest',
        'video' : 'Interested In Videography Contest'
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Contact Number'}),
            'college': forms.TextInput(attrs={'placeholder': 'College'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email ID'}),
            'whatsapp': forms.TextInput(attrs={'placeholder': 'WhatsApp Number'}),
        }


class PhotographyWorkshopForm(forms.ModelForm):
    event_name = "photographyworkshop"
    class Meta:
        model = PhotographyWorkshops
        fields = ['name','phoneNum','email', 'whatsapp', 'basicsofphoto','lightpainting','portrait']

        labels = {
        "name": "",
        "phoneNum": "",
        'email':'',
        'whatsapp':'',

        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Contact Number'}),
            'college': forms.TextInput(attrs={'placeholder': 'College'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email ID'}),
            'whatsapp': forms.TextInput(attrs={'placeholder': 'WhatsApp Number'}),
        }

# Informals

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


# Workshops

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


# Management

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

# Sports

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


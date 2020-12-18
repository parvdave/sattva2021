from django import forms
from .models import *

class SoloSingingForm(forms.ModelForm):
    event_name = "solosinging"
    class Meta:
        model = SoloSinging
        fields = ['name','age','email','country','address','idlink','phoneNum','idlink','whatsapp','contacted']
        labels = {
        "name": "",
        "email": "",
        'age':'',
        'address':'',
        'phoneNum':"",
        'whatsapp':"",
        'country':'',
        'idlink':'Upload your ID proof to imgdb.in and paste the link here',
        'contacted':"Have you already received the details regarding the first phase of the competition (By someone from our team)? (Yes/No) ",
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name','required':'required'}),
            'email':forms.EmailInput(attrs={'placeholder': 'Email','required':'required'}),
            'age':forms.NumberInput(attrs={'placeholder':'Age','required':'required'}),
            'address':forms.Textarea(attrs={'placeholder':'Address','required':'required'}),
            'idlink':forms.URLInput(attrs={'placeholder':'Upload your ID proof to imgdb.in and paste the link here'}),
            'country':forms.TextInput(attrs={'placeholder':'Country','required':'required'}),
        }

class GroupSingingForm(forms.Form):
    event_name = "groupsinging"
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Email Address',max_length=100)
    age = forms.IntegerField(label='Your age',max_value=26,min_value=0)
    # class Meta:
    #     model = GroupSinging
    #     fields = ['name','age','email','country','address','phoneNum','whatsapp','contacted']
    #     labels = {
    #     "name": "Enter your name: ",
    #     "email": "Enter your email: ",
    #     'age':'Enter age: ',
    #     'address':'Enter your address: ',
    #     'phoneNum':"Enter your contact number: ",
    #     'whatsapp':"Enter your whatsapp number: ",
    #     'contacted':"Have you already received the details regarding the first phase of the competition (By someone from our team)? (Yes/No) ",
    #     }

class PoetryForm(forms.ModelForm):
    event_name = "poetry"
    class Meta:
        model = Poetry
        fields = ['name','age','email','country','address','idlink','phoneNum','whatsapp','contacted']
        labels = {
        "name": "",
        "email": "",
        'age':'',
        'address':'',
        'phoneNum':"",
        'whatsapp':"",'idlink':'Upload your ID proof to imgdb.in and paste the link here',
        'country':'',
        'contacted':"Have you already received the details regarding the first phase of the competition (By someone from our team)? (Yes/No) ",
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name','required':'required'}),
            'email':forms.EmailInput(attrs={'placeholder': 'Email','required':'required'}),
            'age':forms.NumberInput(attrs={'placeholder':'Age','required':'required'}),
            'address':forms.Textarea(attrs={'placeholder':'Address','required':'required'}),
            'phoneNum':forms.TextInput(attrs={'placeholder':"Contact Number",'required':'required'}),
            'whatsapp':forms.TextInput(attrs={'placeholder':"Whatsapp Number",'required':'required'}),
            'country':forms.TextInput(attrs={'placeholder':'Country','required':'required'}),
        }

class ShortFilmsForm(forms.ModelForm):
    event_name = "shortfilms"
    class Meta:
        model = ShortFilms
        fields = ['name','nameoffilm','genreoffilm','email','idlink','address','country','phoneNum','whatsapp','contacted']
        labels = {
        "name": "",
        "nameoffilm": "",
        'genreoffilm':'',
        'address':'',
        'email':"",'idlink':'Upload your ID proof to imgdb.in and paste the link here',
        'phoneNum':"",
        'whatsapp':"",
        'country':'',
        'contacted':"Have you already received the details regarding the first phase of the competition (By someone from our team)? (Yes/No) ",
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name of head','required':'required'}),
            'nameoffilm': forms.TextInput(attrs={'placeholder': 'Name of film','required':'required'}),
            'genreoffilm':forms.TextInput(attrs={'placeholder': 'Genre of film','required':'required'}),
            'email':forms.EmailInput(attrs={'placeholder': 'Email','required':'required'}),
            'age':forms.NumberInput(attrs={'placeholder':'Age','required':'required'}),
            'address':forms.Textarea(attrs={'placeholder':'Address','required':'required'}),
            'phoneNum':forms.TextInput(attrs={'placeholder':"Contact Number",'required':'required'}),
            'whatsapp':forms.TextInput(attrs={'placeholder':"Whatsapp Number",'required':'required'}),
            'country':forms.TextInput(attrs={'placeholder':'Country','required':'required'}),
        }

class BeatBoxingForm(forms.ModelForm):
    event_name = "beatboxing"
    class Meta:
        model = BeatBoxing
        fields = ['name','age','email','country','address','idlink','phoneNum','whatsapp','contacted']
        labels = {
        "name": "",
        "email": "",
        'age':'','idlink':'Upload your ID proof to imgdb.in and paste the link here',
        'address':'',
        'phoneNum':"",
        'whatsapp':"",
        'country':'',
        'contacted':"Have you already received the details regarding the first phase of the competition (By someone from our team)? (Yes/No) ",
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name','required':'required'}),
            'email':forms.EmailInput(attrs={'placeholder': 'Email','required':'required'}),
            'age':forms.NumberInput(attrs={'placeholder':'Age','required':'required'}),
            'address':forms.Textarea(attrs={'placeholder':'Address','required':'required'}),
            'country':forms.TextInput(attrs={'placeholder':'Country','required':'required'}),
            'phoneNum':forms.TextInput(attrs={'placeholder':"Contact Number",'required':'required'}),
            'whatsapp':forms.TextInput(attrs={'placeholder':"Whatsapp Number",'required':'required'}),
        }

class MonoActForm(forms.ModelForm):
    event_name = "monoact"
    class Meta:
        model = MonoAct
        fields = ['name','age','email','country','address','idlink','phoneNum','whatsapp','contacted']
        labels = {
        "name": "",
        "email": "",
        'age':'','idlink':'Upload your ID proof to imgdb.in and paste the link here',
        'address':'',
        'phoneNum':"",
        'whatsapp':"",
        'country':'',
        'contacted':"Have you already received the details regarding the first phase of the competition (By someone from our team)? (Yes/No) ",
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name','required':'required'}),
            'email':forms.EmailInput(attrs={'placeholder': 'Email','required':'required'}),
            'age':forms.NumberInput(attrs={'placeholder':'Age','required':'required'}),
            'address':forms.Textarea(attrs={'placeholder':'Address','required':'required'}),
            'country':forms.TextInput(attrs={'placeholder':'Country','required':'required'}),
            'phoneNum':forms.TextInput(attrs={'placeholder':"Contact Number",'required':'required'}),
            'whatsapp':forms.TextInput(attrs={'placeholder':"Whatsapp Number",'required':'required'}),
        }

class RapBattleForm(forms.ModelForm):
    event_name = "rapbattle"
    class Meta:
        model = RapBattle
        fields = ['name','age','email','country','address','idlink','phoneNum','whatsapp','contacted']
        labels = {
        "name": "",
        "email": "",
        'age':'','idlink':'Upload your ID proof to imgdb.in and paste the link here',
        'address':'',
        'phoneNum':"",
        'whatsapp':"",
        'country':'',
        'contacted':"Have you already received the details regarding the first phase of the competition (By someone from our team)? (Yes/No) ",
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name','required':'required'}),
            'email':forms.EmailInput(attrs={'placeholder': 'Email','required':'required'}),
            'age':forms.NumberInput(attrs={'placeholder':'Age','required':'required'}),
            'address':forms.Textarea(attrs={'placeholder':'Address','required':'required'}),
            'country':forms.TextInput(attrs={'placeholder':'Country','required':'required'}),
            'phoneNum':forms.TextInput(attrs={'placeholder':"Contact Number",'required':'required'}),
            'whatsapp':forms.TextInput(attrs={'placeholder':"Whatsapp Number",'required':'required'}),
        }

class ClassicalDanceForm(forms.ModelForm):
    event_name = "classicaldance"
    class Meta:
        model = ClassicalDance
        fields = ['name','age','email','country','address','idlink','style','phoneNum','whatsapp','contacted']
        labels = {
        "name": "",
        "email": "",
        'age':'',
        'address':'','idlink':'Upload your ID proof to imgdb.in and paste the link here',
        'phoneNum':"",
        'whatsapp':"",
        'style':"",
        'contacted':"Have you already received the details regarding the first phase of the competition (By someone from our team)? (Yes/No) ",
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name','required':'required'}),
            'email':forms.EmailInput(attrs={'placeholder': 'Email','required':'required'}),
            'age':forms.NumberInput(attrs={'placeholder':'Age','required':'required'}),
            'address':forms.Textarea(attrs={'placeholder':'Address','required':'required'}),
            'country':forms.TextInput(attrs={'placeholder':'Country','required':'required'}),
            'style':forms.TextInput(attrs={'placeholder':'Style of Dance','required':'required'}),
            'phoneNum':forms.TextInput(attrs={'placeholder':"Contact Number",'required':'required'}),
            'whatsapp':forms.TextInput(attrs={'placeholder':"Whatsapp Number",'required':'required'}),
        }

class WesternDanceForm(forms.ModelForm):
    event_name = "westerndance"
    class Meta:
        model = WesternDance
        fields = ['name','age','email','country','address','idlink','style','phoneNum','whatsapp','contacted']
        labels = {
        "name": "",
        "email": "",
        'age':'',
        'address':'',
        'phoneNum':"",
        'style':"",'idlink':'Upload your ID proof to imgdb.in and paste the link here',
        'whatsapp':"",
        'country':"",
        'contacted':"Have you already received the details regarding the first phase of the competition (By someone from our team)? (Yes/No) ",
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name','required':'required','required':'required'}),
            'email':forms.EmailInput(attrs={'placeholder': 'Email','required':'required'}),
            'age':forms.NumberInput(attrs={'placeholder':'Age','required':'required'}),
            'address':forms.Textarea(attrs={'placeholder':'Address','required':'required'}),
            'country':forms.TextInput(attrs={'placeholder':'Country','required':'required'}),
            'style':forms.TextInput(attrs={'placeholder':'Style of Dance','required':'required'}),
            'phoneNum':forms.TextInput(attrs={'placeholder':"Contact Number",'required':'required'}),
            'whatsapp':forms.TextInput(attrs={'placeholder':"Whatsapp Number",'required':'required'}),
        }

# Photography

class PhotographyContestForm(forms.ModelForm):
    event_name = "photographycontest"
    class Meta:
        model = PhotographyContest
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
            'name': forms.TextInput(attrs={'placeholder': 'Name','required':'required'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Contact Number','required':'required'}),
            'college': forms.TextInput(attrs={'placeholder': 'College','required':'required'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email ID','required':'required'}),
            'whatsapp': forms.TextInput(attrs={'placeholder': 'WhatsApp Number','required':'required'}),
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
            'name': forms.TextInput(attrs={'placeholder': 'Name','required':'required'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Contact Number','required':'required'}),
            'college': forms.TextInput(attrs={'placeholder': 'College','required':'required'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email ID','required':'required'}),
            'whatsapp': forms.TextInput(attrs={'placeholder': 'WhatsApp Number','required':'required'}),
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
            'name1': forms.TextInput(attrs={'placeholder': 'Name of Participant 1','required':'required'}),
            'phoneNum1': forms.TextInput(attrs={'placeholder': 'Contact number of Participant 1','required':'required'}),
            'college1': forms.TextInput(attrs={'placeholder': 'Name of College 1','required':'required'}),
            'city1': forms.TextInput(attrs={'placeholder': 'City of Residence (Participant 1)','required':'required'}),
            'gender1': forms.RadioSelect(attrs={'required':'required'}),
            'name2': forms.TextInput(attrs={'placeholder': 'Name of Participant 1','required':'required'}),
            'phoneNum2': forms.TextInput(attrs={'placeholder': 'Contact number of Participant 2','required':'required'}),
            'college2': forms.TextInput(attrs={'placeholder': 'Name of College 2','required':'required'}),
            'city2': forms.TextInput(attrs={'placeholder': 'City of Residence (Participant 2)','required':'required'}),
            'gender2': forms.RadioSelect(attrs={'required':'required'}),
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
            'name': forms.TextInput(attrs={'placeholder': 'Name of Participant 1','required':'required'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Contact number of Participant 1','required':'required'}),
            'college': forms.TextInput(attrs={'placeholder': 'Name of College 1','required':'required'}),
            'city': forms.TextInput(attrs={'placeholder': 'City of Residence (Participant 1)','required':'required'}),
            'gender': forms.RadioSelect(attrs={'required':'required'}),
            'talent': forms.TextInput(attrs={'placeholder':'Talents (eg. Singing, dancing)','required':'required'}),
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
            'name': forms.TextInput(attrs={'placeholder': 'Name of Participant 1','required':'required'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Contact number of Participant 1','required':'required'}),
            'college': forms.TextInput(attrs={'placeholder': 'Name of College 1','required':'required'}),
            'city': forms.TextInput(attrs={'placeholder': 'City of Residence (Participant 1)','required':'required'}),
            'gender': forms.RadioSelect(attrs={'required':'required'}),
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
            'name': forms.TextInput(attrs={'placeholder': 'Name','required':'required'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Contact Number','required':'required'}),
            'college': forms.TextInput(attrs={'placeholder': 'College Name','required':'required'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Id','required':'required'}),
            'age':forms.NumberInput(attrs={'placeholder':'Age','required':'required'}),
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
            'name': forms.TextInput(attrs={'placeholder': 'Name','required':'required'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Contact Number','required':'required'}),
            'college': forms.TextInput(attrs={'placeholder': 'College Name','required':'required'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Id','required':'required'}),
            'age':forms.NumberInput(attrs={'placeholder':'Age','required':'required'}),
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
            'name': forms.TextInput(attrs={'placeholder': 'Name','required':'required'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Contact Number','required':'required'}),
            'college': forms.TextInput(attrs={'placeholder': 'College Name','required':'required'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Id','required':'required'}),
            'age':forms.NumberInput(attrs={'placeholder':'Age','required':'required'}),
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
            'name': forms.TextInput(attrs={'placeholder': 'Name','required':'required'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Contact Number','required':'required'}),
            'college': forms.TextInput(attrs={'placeholder': 'College Name','required':'required'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Id','required':'required'}),
            'age':forms.NumberInput(attrs={'placeholder':'Age','required':'required'}),
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
            'name': forms.TextInput(attrs={'placeholder': 'Name','required':'required'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Contact Number','required':'required'}),
            'college': forms.TextInput(attrs={'placeholder': 'College Name','required':'required'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Id','required':'required'}),
            'age':forms.NumberInput(attrs={'placeholder':'Age','required':'required'}),
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
            'name1': forms.TextInput(attrs={'placeholder': 'Name','required':'required'}),
            'phoneNum1': forms.TextInput(attrs={'placeholder': 'Contact Number','required':'required'}),
            'college1': forms.TextInput(attrs={'placeholder': 'College Name','required':'required'}),
            'email1': forms.EmailInput(attrs={'placeholder': 'Email Id','required':'required'}),
            'name2': forms.TextInput(attrs={'placeholder': 'Name of 2nd Participant','required':'required'}),
            'phoneNum2': forms.TextInput(attrs={'placeholder': 'Contact Number of 2nd Participant','required':'required'}),
            'college2': forms.TextInput(attrs={'placeholder': 'College Name of 2nd Participant','required':'required'}),
            'email2': forms.EmailInput(attrs={'placeholder': 'Email Id of 2nd Participant','required':'required'}),
            'name3': forms.TextInput(attrs={'placeholder': 'Name of 3rd Participant','required':'required'}),
            'phoneNum3': forms.TextInput(attrs={'placeholder': 'Contact Number of 3rd Participant','required':'required'}),
            'college3': forms.TextInput(attrs={'placeholder': 'College Name of 3rd Participant','required':'required'}),
            'email3': forms.EmailInput(attrs={'placeholder': 'Email Id of 3rd Participant','required':'required'}),
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
            'name': forms.TextInput(attrs={'placeholder': 'Name','required':'required'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Contact Number','required':'required'}),
            'college': forms.TextInput(attrs={'placeholder': 'College Name','required':'required'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Id','required':'required'}),
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
            'name1': forms.TextInput(attrs={'placeholder': 'Name','required':'required'}),
            'phoneNum1': forms.TextInput(attrs={'placeholder': 'Contact Number','required':'required'}),
            'college1': forms.TextInput(attrs={'placeholder': 'College Name','required':'required'}),
            'email1': forms.EmailInput(attrs={'placeholder': 'Email Id','required':'required'}),
            'name2': forms.TextInput(attrs={'placeholder': 'Name of 2nd Participant','required':'required'}),
            'phoneNum2': forms.TextInput(attrs={'placeholder': 'Contact Number of 2nd Participant','required':'required'}),
            'college2': forms.TextInput(attrs={'placeholder': 'College Name of 2nd Participant','required':'required'}),
            'email2': forms.EmailInput(attrs={'placeholder': 'Email Id of 2nd Participant','required':'required'}),
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
            'name': forms.TextInput(attrs={'placeholder': 'Name','required':'required'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Contact Number','required':'required'}),
            'college': forms.TextInput(attrs={'placeholder': 'College Name','required':'required'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Id','required':'required'}),
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
            'name1': forms.TextInput(attrs={'placeholder': 'Name','required':'required'}),
            'phoneNum1': forms.TextInput(attrs={'placeholder': 'Contact Number','required':'required'}),
            'college1': forms.TextInput(attrs={'placeholder': 'College Name','required':'required'}),
            'email1': forms.EmailInput(attrs={'placeholder': 'Email Id','required':'required'}),
            'name2': forms.TextInput(attrs={'placeholder': 'Name of 2nd Participant','required':'required'}),
            'phoneNum2': forms.TextInput(attrs={'placeholder': 'Contact Number of 2nd Participant','required':'required'}),
            'college2': forms.TextInput(attrs={'placeholder': 'College Name of 2nd Participant','required':'required'}),
            'email2': forms.EmailInput(attrs={'placeholder': 'Email Id of 2nd Participant','required':'required'}),
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
            'name': forms.TextInput(attrs={'placeholder': 'Name','required':'required'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Contact Number','required':'required'}),
            'college': forms.TextInput(attrs={'placeholder': 'College Name','required':'required'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Id','required':'required'}),
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
            'name': forms.TextInput(attrs={'placeholder': 'Name','required':'required'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Contact Number','required':'required'}),
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
            'name1': forms.TextInput(attrs={'placeholder': 'Name','required':'required'}),
            'phoneNum1': forms.TextInput(attrs={'placeholder': 'Contact Number','required':'required'}),
            'rank1': forms.TextInput(attrs={'placeholder': 'Your Rank','required':'required'}),
            'name2': forms.TextInput(attrs={'placeholder': 'Name of 2nd Participant','required':'required'}),
            'phoneNum2': forms.TextInput(attrs={'placeholder': 'Contact Number of 2nd Participant','required':'required'}),
            'rank2': forms.TextInput(attrs={'placeholder': 'Rank of 2nd Participant','required':'required'}),
            'name3': forms.TextInput(attrs={'placeholder': 'Name of 3rd Participant','required':'required'}),
            'phoneNum3': forms.TextInput(attrs={'placeholder': 'Contact Number of 3rd Participant','required':'required'}),
            'rank3': forms.TextInput(attrs={'placeholder': 'Rank of 3rd Participant','required':'required'}),
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
            'name1': forms.TextInput(attrs={'placeholder': 'Name','required':'required'}),
            'phoneNum1': forms.TextInput(attrs={'placeholder': 'Contact Number','required':'required'}),
            'tier1': forms.TextInput(attrs={'placeholder': 'Your Tier','required':'required'}),
            'name2': forms.TextInput(attrs={'placeholder': 'Name of 2nd Participant','required':'required'}),
            'phoneNum2': forms.TextInput(attrs={'placeholder': 'Contact Number of 2nd Participant','required':'required'}),
            'tier2': forms.TextInput(attrs={'placeholder': 'Tier of 2nd Participant','required':'required'}),
            'name3': forms.TextInput(attrs={'placeholder': 'Name of 3rd Participant','required':'required'}),
            'phoneNum3': forms.TextInput(attrs={'placeholder': 'Contact Number of 3rd Participant','required':'required'}),
            'tier3': forms.TextInput(attrs={'placeholder': 'Tier of 3rd Participant','required':'required'}),
            'name4': forms.TextInput(attrs={'placeholder': 'Name of 4th Participant','required':'required'}),
            'phoneNum4': forms.TextInput(attrs={'placeholder': 'Contact Number of 4th Participant','required':'required'}),
            'tier4': forms.TextInput(attrs={'placeholder': 'Tier of 4th Participant','required':'required'}),
        }


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


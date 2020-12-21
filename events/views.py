from django.shortcuts import render,redirect
from .forms import *
from django.core.mail import send_mail,EmailMessage
from django.views.generic import TemplateView
from sattva.settings import EMAIL_HOST_USER
from django.urls import reverse
from django.conf.urls import static
from .models import Event

# Create your views here.
class Renderform(TemplateView):
    def get(self,request,event):
        
        dict_event = {'solosinging':SoloSingingForm(),'rapbattle':RapBattleForm(),'groupsinging':GroupSingingForm(),'shortfilms':ShortFilmsForm(),'poetry':PoetryForm(),'groupsinging':GroupSingingForm(),'beatboxing':BeatBoxingForm(),'classicaldance':ClassicalDanceForm(),'westerndance':WesternDanceForm(),'monoact':MonoActForm()}
        dict_event.update({'advision':AdVisionForm(),"turnaround":TurnaroundForm(),"houseofbattle":HouseOfBattleForm(),"tazhakhabar":TazhaKhabarForm(),"bidweiser":BidweiserForm(),"marketguru":MarketGuruForm()})
        dict_event.update({'standupworkshop':StandUpWorkshopForm(),'influentialtrends':InfluentialTrendsWorkshopForm(),'danceworkshop':DanceWorkshopForm(),'fitnessworkshop':FitnessWorkshopForm(),'actingworkshop':ActingWorkshopForm()})
        dict_event.update({"fifa":FifaForm(),'rocketleague':RocketLeagueForm(),'pubg':PUBGForm()})
        dict_event.update({'popculture':PopCultureForm(),'punintended':PunIntendedForm(),'mrmssattva':MrMsSattvaForm()})
        dict_event.update({'photographycontests':PhotographyContestForm(),'photographyworkshops':PhotographyWorkshopForm()})
        dict_event.update({'charadeswithatwist':CharadesForm(),'glamup':GlamUpForm()})
        form = dict_event[event]
        if 'photography' in event:
            eventModel = Event.objects.all().filter(eventslug__icontains=event).first()
            if 'contest' in event:
                contests_rules = eventModel.rules.split('|')
                for i in range(len(contests_rules)):
                    contests_rules[i] = contests_rules[i].split(':')
                    contests_rules[i][1] = contests_rules[i][1].split('##')
                contests_details = eventModel.desc.split('|')
                for i in range(len(contests_details)):
                    contests_details[i] = contests_details[i].split(':')
                return render(request,'events/eventform.html',{'form':form,'event':eventModel,'rules':contests_rules,'desc':contests_details})
            else:
                workshops_details = eventModel.desc.split('|')
                for i in range(len(workshops_details)):
                    workshops_details[i] = workshops_details[i].split(':')
        eventModel = Event.objects.all().filter(eventslug__icontains=event).first()
        return render(request,'events/eventform.html',{'form':form,'event':eventModel,'rules':eventModel.rules.split('.')[:-1]})
        
            # return render(request,'events/sorry.html',{})

        # return render(request,'events/eventform.html',{'form':form,'rules':eventModel.rules.split('.'),'desc':eventModel.desc,'script':eventModel.url})
    def post(self,request,event):
        dict_event = {'solosinging':SoloSingingForm(request.POST),'shortfilms':ShortFilmsForm(request.POST),'poetry':PoetryForm(request.POST),'groupsinging':GroupSingingForm(request.POST),'beatboxing':BeatBoxingForm(request.POST),'classicaldance':ClassicalDanceForm(request.POST),'westerndance':WesternDanceForm(request.POST),'monoact':MonoActForm(request.POST)}
        dict_event.update({'advision':AdVisionForm(request.POST),"turnaround":TurnaroundForm(request.POST),"houseofbattle":HouseOfBattleForm(request.POST),"tazhakhabar":TazhaKhabarForm(request.POST),"bidweiser":BidweiserForm(request.POST),"marketguru":MarketGuruForm(request.POST)})
        dict_event.update({'standupworkshop':StandUpWorkshopForm(request.POST),'influentialtrends':InfluentialTrendsWorkshopForm(request.POST),'danceworkshop':DanceWorkshopForm(request.POST),'fitnessworkshop':FitnessWorkshopForm(request.POST),'actingworkshop':ActingWorkshopForm(request.POST)})
        dict_event.update({"fifa":FifaForm(request.POST),'rocketleague':RocketLeagueForm(request.POST),'pubg':PUBGForm(request.POST)})
        dict_event.update({'popculture':PopCultureForm(request.POST),'punintended':PunIntendedForm(request.POST),'mrmssattva':MrMsSattvaForm(request.POST)})
        dict_event.update({'photographycontests':PhotographyContestForm(request.POST),'photographyworkshops':PhotographyWorkshopForm(request.POST)})
        form = dict_event[event]
        if form.is_valid() == True:
            if 'email' in form.fields:
                recepient = str(form['email'].value())
                mail_content = f"""<!DOCTYPE html>
                <html lang="en">

                <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    @import url("https://fonts.googleapis.com/css2?family=Work+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap%22);
                </style>
                <title>Document</title>
                </head>

                <body style="

                width: 700px;
                margin: 0 auto;
                overflow-y: scroll;
                overflow-x: hidden;
                font-family: ' Work Sans', Arial, sans-serif; position: relative;
                margin-bottom: 30px;">
                <header style="  text-align: center;  margin: 50px auto 30px;">
                    <h1 style="display: inline-block;">Sattva'<small style="font-size: 0.7em;">21</small></h1>
                </header>

                <main>
                    <div class="homeSlide" style="background: #ffd3e0 !important;
                    width: 100%;
                    height: auto;
                    padding: 30px;
                    border-radius: 20px;
                    padding-bottom: 70px;">

                    <div class="image" style="width: 420px;
                    height: 400px;
                    margin: 0 auto;">
                        <img src="https://i.imgur.com/5zDItAW.png" alt="" style="width: 90%;">
                    </div>


                    <h1 style="text-align: center;">Hi {request.POST.get('name')},
                        <br>
                        Welcome To XYZ Event
                    </h1>
                    <br>
                    <p style="text-align: center;
                    font-size: 1.5em;">Thanks For Registering</p>
                    </div>
                </main>
                </body>
                </html>"""
                msg = EmailMessage('Hi brotheriinoo',mail_content, EMAIL_HOST_USER, [recepient])
                msg.content_subtype = "html"
                html_content = '<p>This is an <strong>important</strong> message.</p>'
                msg.send()
                # subject = 'hi deer'
                # message = 'Hope you are enjoying your Django Tutorials'
                # send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
                return render(request,'events/success.html',{'recepient':recepient})
        return render(request,'events/eventform.html',{'form':form,'notvalid':'notvalid'})
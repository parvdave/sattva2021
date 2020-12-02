from django.shortcuts import render,redirect
from .forms import SoloSingingForm
from django.core.mail import send_mail,EmailMessage
from django.views.generic import TemplateView
from sattva.settings import EMAIL_HOST_USER


# Create your views here.
class Renderform(TemplateView):
    def get(self,request):
        form = SoloSingingForm()
        return render(request,'events/eventform.html',{'form':form})
    def post(self,request):
        form = SoloSingingForm(request.POST)
        if form.is_valid():
            recepient = str(form['email'].value())
            mail_content = """<!DOCTYPE html>
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


            <h1 style="text-align: center;">Hi Vrushit Patel,
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
            msg.send()

            # subject = 'hi deer'
            # message = 'Hope you are enjoying your Django Tutorials'
            # send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
            return render(request,'events/success.html',{'recepient':recepient})
        return render(request,'events/eventform.html',{'form':form})
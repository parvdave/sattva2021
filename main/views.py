from django.shortcuts import render
from core.models import Member
# Create your views here.



def home(request):
    depts = [i['deptName'] for i in Member.objects.values('deptName').order_by('deptName').distinct()]
    depts.remove('Super Core')
    supercoredept = 'Super Core'
    return render(request,'main/index.html',{'depts':depts,'supercoredept':supercoredept,'singq':"'"})
from django.shortcuts import render
from core.models import Member
from .models import DepartmentEventIsland
from events.models import Event
# Create your views here.



def home(request):
    depts = [i['deptName'] for i in Member.objects.values('deptName').order_by('deptName').distinct()]
    depts.remove('Super Core')
    supercoredept = 'Super Core'
    return render(request,'main/index.html',{'depts':depts,'supercoredept':supercoredept,'singq':"'"})

def islandview(request,dept):
    dept = dept.title()
    dictnum = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8}
    events = DepartmentEventIsland.objects.all().filter(deptslug__icontains=dept)
    eventsfull = Event.objects.all().filter(deptName__icontains=dept)
    argument = dictnum[events[0].deptid]
    return render(request,'main/island.html',{'dept':dept,'argument':argument,'deptdeets':events[0],'events':events})
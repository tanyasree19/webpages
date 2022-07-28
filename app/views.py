from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.db.models.functions import Length

from app.models import *
def insert_topic(request):
    t=Topic.objects.get_or_create(topic_name='Kabaddi')[0]
    t.save()
    return HttpResponse('Topic is added successfully')

def insert_webpage(request):
    t1=Topic.objects.get_or_create(Topic_name='Kabaddi')[0]
    t1.save()
    w=Webpage.objects.get_or_create(Topic_name=t1,name='JPG',url='https://jpg.com')[0]
    w.save()
    return HttpResponse('Webpage data is inserted')

def display_Topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_Topics.html',d)

def display_webpage(request):
    LOW=Webpage.objects.all()
    #LOW=Webpage.objects.filter(topic_name='V Ball')
    #LOW=Webpage.objects.exclude(topic_name='V Ball')
    #LOW=Webpage.objects.all()[:5:]
    LOW=Webpage.objects.all().order_by('name')  
    LOW=Webpage.objects.all().order_by('-name')
    LOW=Webpage.objects.all().order_by(Length('name'))
    LOW=Webpage.objects.all().order_by(Length('name').desc())

    d={'webpage':LOW}
    return render(request,'display_webpage.html',d)

def display_access(request):
    LOA=Access_Records.objects.all()
    LOA=Access_Records.objects.filter(date='1990-01-12')
    LOA=Access_Records.objects.filter(date__gte='1990-01-12')
    LOA=Access_Records.objects.filter(date__lte='1990-01-12')
    LOA=Access_Records.objects.filter(date__year='1980')
    LOA=Access_Records.objects.filter(date__month='01')
    LOA=Access_Records.objects.filter(date__day='12')
    LOA=Access_Records.objects.filter(date__year__gt='1990')



    
    d={'access':LOA}
    return render(request,'display_access.html',d)






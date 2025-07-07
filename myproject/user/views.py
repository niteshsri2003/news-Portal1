
from django.db.models import Q
from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.

def index(request):
    data=category.objects.all().order_by('id')[0:12]
    ndata=tbl_news.objects.all().order_by('-id')[0:12]
    ndata1=tbl_news.objects.all().order_by('-id')[0:3]
    data1=tbl_city.objects.all().order_by('-id')[0:24]
    sliderdata=tbl_slider.objects.all().order_by('-id')[0:3]
    md={'cdata':data,'newsdata':ndata,'citydata':data1,'lndata':ndata1,'sdata':sliderdata}

    return render(request,'index.html',md)

def about(request):
    return render(request,'about.html')

def contact(request):
   md={}
   if request.method=="POST":
       a=request.POST.get('name')
       b=request.POST.get('email')
       c=request.POST.get('mobile')
       d=request.POST.get('msg')
       contactus(Name=a,Message=d,Email=b,Mobile=c).save()
       return HttpResponse("<script>alert('Thanks for contacting with us....');location.href='/contact/';</script>")


       #md={"name":a,"email":b,"mobile":c,"message":d}

   return render(request,'contact.html')

def faqs(request):
    return render(request,'faqs.html')

def jobs(request):
    jdata=tbl_jobs.objects.all().order_by('-id')
    mydict={"jobsdata":jdata}
    return render(request,'jobs.html',mydict)


def login(request):
    return render(request,'login.html')

def news(request):
    catid=request.GET.get('catid')
    cityid=request.GET.get('cityid')
    searchdata=request.GET.get('search')
    data=""
    if catid is not None:
        data=tbl_news.objects.all().filter(news_category=catid)
    elif cityid is not None:
        data=tbl_news.objects.all().filter(news_city=cityid)
    elif searchdata is not None:
        data=tbl_news.objects.all().filter(Q(headline__icontains=searchdata)|Q(news_descriptions__icontains=searchdata)|Q(news_city__city_name__icontains=searchdata)|Q(news_category__category_name__icontains=searchdata))
    else:
        data=tbl_news.objects.all().order_by('-id')

    citydata=tbl_city.objects.all().order_by('-id')
    categorydata=category.objects.all().order_by('-id')
    mydict={"ndata":data,'citydata':citydata,'categorydata':categorydata}
    return render(request,'news.html',mydict)

def videonews(request):
    data=video_news.objects.all().order_by('-id')
    mydict={"vdata":data,}
    return render(request,'videonews.html',mydict)
def news(request):
    catid=request.GET.get('catid')
    cityid=request.GET.get('cityid')
    searchdata=request.GET.get('search')
    data=""
    if catid is not None:
        data=tbl_news.objects.all().filter(news_category=catid)
    elif cityid is not None:
        data=tbl_news.objects.all().filter(news_city=cityid)
    elif searchdata is not None:
        data=tbl_news.objects.all().filter(Q(headline__icontains=searchdata)|Q(news_descriptions__icontains=searchdata)|Q(news_city__city_name__icontains=searchdata)|Q(news_category__category_name__icontains=searchdata))
    else:
        data=tbl_news.objects.all().order_by('-id')
    citydata=tbl_city.objects.all().order_by('-id')
    categorydata=category.objects.all().order_by('-id')
    mydict={'ndata':data,'citydata':citydata,'categorydata':categorydata}
    return render(request,'news.html',mydict)




def newsdetails(request):
    x=request.GET.get('nid')
    sid=request.GET.get('sid')
    data=""
    sdata=""
    if x is not None:
        data=tbl_news.objects.all().filter(id=x)
    if sid is not None:
        sdata=tbl_slider.objects.all().filter(id=sid)
    mydict={"ndata":data,'sdata':sdata}
    return render(request,'newsdetails.html',mydict)
def portfolio(request):
    return render(request,'myprofile.html')
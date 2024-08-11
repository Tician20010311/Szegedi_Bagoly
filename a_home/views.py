from django.shortcuts import render
from .models import *

def home_view(request):
    themes = Theme.objects.filter(is_active=True)
    return render(request, 'home.html',{'themes':themes})

def chat_view(request):
    themes = Theme.objects.filter(is_active=True)
    return render(request, 'chat.html',{'themes':themes})

def enroll(request):
    themes = Theme.objects.filter(is_active=True)
    return render(request, 'enroll.html',{'themes':themes})

def digital(request):
    themes = Theme.objects.filter(is_active=True)
    return render(request, 'digital.html',{'themes':themes})

def without_border(request):
    themes = Theme.objects.filter(is_active=True)
    objects = Withoutborders.objects.all()
    data = []
    
    for obj in objects:
        if obj.days == "1":
            url = "/firstday"
        elif obj.days == "2":
            url = "/secondday"
        elif obj.days == "3":
            url = "/thirdday"
        elif obj.days == "4":
            url = "/fourthday"
        elif obj.days == "5":
            url = "/fifthday"
        else:
            url = "/defaultday"  # Alapértelmezett érték, ha egyik feltétel sem teljesül

        data.append({'object': obj, 'url': url})
    
    context = {
        'themes': themes,
        'data': data,  # Adatok átadása a sablonnak
    }
    
    return render(request, 'without_border.html', context)

def about(request):
    themes = Theme.objects.filter(is_active=True)
    return render(request, 'about.html',{'themes':themes})

def news(request):
    leadnews = LeadNews.objects.all()
    themes = Theme.objects.filter(is_active=True)
    firstnews = []
    secondnews = []
    for index, item in enumerate(leadnews):
        if index % 2 == 0:
            firstnews.append(item)
        else:
            secondnews.append(item)
    return render(request, "news.html", {'firstnews': firstnews, 'secondnews': secondnews,'leadnews':leadnews,'themes':themes,})


def dayone(request):
    themes = Theme.objects.filter(is_active=True)
    image = Firstday.objects.all()
    firstimage = []
    secondimage = []
    thirdimage = []
    for index, item in enumerate(image):
        if index % 3 == 0:
            firstimage.append(item)
        elif index % 2 == 0:
            secondimage.append(item)
        else:
            thirdimage.append(item)
    return render(request, "firstday.html", {'firstimage': firstimage, 'secondimage': secondimage,'thirdimage':thirdimage,'themes':themes,})

def daytwo(request):
    themes = Theme.objects.filter(is_active=True)
    image = Secondday.objects.all()
    firstimage = []
    secondimage = []
    thirdimage = []
    for index, item in enumerate(image):
        if index % 3 == 0:
            firstimage.append(item)
        elif index % 2 == 0:
            secondimage.append(item)
        else:
            thirdimage.append(item)
    return render(request, "secondday.html", {'firstimage': firstimage, 'secondimage': secondimage,'thirdimage':thirdimage,'themes':themes,})

def daythree(request):
    themes = Theme.objects.filter(is_active=True)
    image = Thirdday.objects.all()
    firstimage = []
    secondimage = []
    thirdimage = []
    for index, item in enumerate(image):
        if index % 3 == 0:
            firstimage.append(item)
        elif index % 2 == 0:
            secondimage.append(item)
        else:
            thirdimage.append(item)
    return render(request, "thirdday.html", {'firstimage': firstimage, 'secondimage': secondimage,'thirdimage':thirdimage,'themes':themes,})

def dayfour(request):
    themes = Theme.objects.filter(is_active=True)
    image = Fourthday.objects.all()
    firstimage = []
    secondimage = []
    thirdimage = []
    for index, item in enumerate(image):
        if index % 3 == 0:
            firstimage.append(item)
        elif index % 2 == 0:
            secondimage.append(item)
        else:
            thirdimage.append(item)
    return render(request, "fouthday.html", {'firstimage': firstimage, 'secondimage': secondimage,'thirdimage':thirdimage,'themes':themes,})

def dayfive(request):
    themes = Theme.objects.filter(is_active=True)
    image = Fiftday.objects.all()
    firstimage = []
    secondimage = []
    thirdimage = []
    for index, item in enumerate(image):
        if index % 3 == 0:
            firstimage.append(item)
        elif index % 2 == 0:
            secondimage.append(item)
        else:
            thirdimage.append(item)
    return render(request, "fifthday.html", {'firstimage': firstimage, 'secondimage': secondimage,'thirdimage':thirdimage,'themes':themes,})
import datetime
from os import listdir
import os
from django.http import HttpResponse
from django.shortcuts import render, reverse

# Create your views here.
def home_view(request):
    template_name = 'app\home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    

    context = {
        'pages': pages
    }
    
    return render(request, template_name, context)


def time(request):
    current_time = datetime.datetime.now().date()

    return HttpResponse(f"Текущее время: {current_time}")


def workdir(request):
    content = os.listdir()
    content_str = '; '.join(content)
    
    return HttpResponse(content_str)
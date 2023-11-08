from django.shortcuts import render
from django.utils import timezone
from mainapp.models import *
# Create your views here.


def index(request):
    title = 'Главная'
    chunk = Chunk.objects.filter(code='about_nedk').first()
    services = Service.objects.all().order_by('ordering')
    clients = Client.objects.all().order_by('ordering')

    return render(request, 'mainapp/index.html', {
        'title': title,
        'chunk': chunk,
        'services': services,
        'clients': clients,
    })


def services(request):
    title = 'Услуги'
    services = Service.objects.all().order_by('ordering')

    return render(request, 'mainapp/services.html', {
        'title': title,
        'services': services,
    })


def contacts(request):
    title = 'Контакты'
    return render(request, 'mainapp/contacts.html', {
        'title': title,
    })

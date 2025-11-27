from django.shortcuts import render
from django.utils import timezone
from mainapp.models import *

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import FeedbackCreateForm
from modules.services.email import send_contact_email_message
from modules.services.utils import get_client_ip
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

def portfolio(request):
    title = 'Портфолио'
    portfolio = Portfolio.objects.all().order_by('ordering')

    return render(request, 'mainapp/portfolio.html', {
        'title': title,
        'portfolio': portfolio,
    })

def accreditation(request):
    title = 'Аккредитация ИТ'
    chunk = Chunk.objects.filter(code='accreditation').first()
    # services = Service.objects.all().order_by('ordering')
    # clients = Client.objects.all().order_by('ordering')

    return render(request, 'mainapp/accreditation.html', {
        'title': title,
        'chunk': chunk,
        # 'services': services,
        # 'clients': clients,
    })

def contacts(request):
    title = 'Контакты'
    contacts = Contacts.objects.all().first()
    return render(request, 'mainapp/contacts.html', {
        'title': title,
        'contacts': contacts,
    })


class FeedbackCreateView(SuccessMessageMixin, CreateView):
    model = Feedback
    form_class = FeedbackCreateForm
    success_message = 'Ваше письмо успешно отправлено администрации сайта'
    template_name = 'mainapp/feedback.html'
    extra_context = {'title': 'Ваш запрос'}
    success_url = reverse_lazy('feedback')

    def form_valid(self, form):
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.ip_address = get_client_ip(self.request)
            # if self.request.user.is_authenticated:
            #     feedback.user = self.request.user
            send_contact_email_message(feedback.subject, feedback.name, feedback.phone, feedback.email, feedback.content, feedback.service, feedback.ip_address)
        return super().form_valid(form)

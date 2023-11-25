from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from taskmanager.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from django.views.generic import ListView


def index(request):
    return render(request, 'main/index.html')


def portfolio(request):
    return render(request, 'main/portfolio.html')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['name']
            subject2 = form.cleaned_data['lastname']
            sender = form.cleaned_data['sender']
            subject3 = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(f'{subject}_{subject2}', f'тема: {subject3}\n сообщение: {message} от {sender} ',
                          DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return HttpResponseRedirect('contact')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, 'main/contact.html', {'form': form})


def portrait_photography(request):
    return render(request, 'main/portrait-photography.html')


def report_photography(request):
    return render(request, 'main/report-photography.html')


def genre_photography(request):
    return render(request, 'main/genre-photography.html')


def street_photography(request):
    return render(request, 'main/street-photography.html')


def bw_photography(request):
    return render(request, 'main/bw-photography.html')

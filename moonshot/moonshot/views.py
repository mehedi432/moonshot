from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'core/index.html')


def send_main(request):
    if request.method == 'POST':
        legal_form = request.POST['legal_form']
        send_mail(legal_form, 'This is text mail', 'moonshot432@gmail.com', ['moonshot432@gmail.com'])
        return redirect('index')
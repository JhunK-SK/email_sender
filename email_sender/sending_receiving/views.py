from django.shortcuts import render
from .forms import EmailForm
from email_sender.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


def index(request):
    
    return render(request, 'sending_receiving/index.html')


def send_one(request):
    form = EmailForm()
    
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            recepient = form.cleaned_data.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            send_mail(
                subject,
                message,
                EMAIL_HOST_USER,
                [recepient],
                fail_silently=False, 
            )
            print(type(form['email'].value()), recepient, subject, message)
            context = {'recepient': recepient}
            return render(request, 'sending_receiving/success.html', context)
    
    context = {'form': form}
    return render(request, 'sending_receiving/sending_one.html', context)


def receiving(request):
    context = {}
    return render(request, 'sending_receiving/receiving.html', context)

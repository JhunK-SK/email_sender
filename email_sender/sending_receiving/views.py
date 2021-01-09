from django.shortcuts import render
from .forms import EmailForm
from email_sender.settings import EMAIL_HOST_USER
from django.core.mail import send_mail, EmailMessage


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
            # print(type(form['email'].value()), recepient, subject, message)
            context = {'recepient': recepient}
            return render(request, 'sending_receiving/success.html', context)
    
    context = {'form': form}
    return render(request, 'sending_receiving/sending_one.html', context)


def receiving(request):
    form = EmailForm()
    
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            from_who = form.cleaned_data.get('email')
            message += " from: " + from_who
            send_mail(
                subject,
                message,
                EMAIL_HOST_USER,
                [EMAIL_HOST_USER],
                fail_silently=False,
            )
            print(from_who, subject, message)
            return render(request, 'sending_receiving/success.html')
            
    context = {'form': form}
    return render(request, 'sending_receiving/receiving.html', context)


def send_file(request):
    form = EmailForm()
    
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            recepient = form.cleaned_data.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            email = EmailMessage(
                subject,
                message,
                EMAIL_HOST_USER,
                [recepient],
                headers={
                    'Message-ID': 'TEST',
                }
            )
            email.content_subtype = 'html'
            
            file = request.FILES['file']
            email.attach(file.name, file.read(), file.content_type)
            
            email.send()
            
            context = {'recepient': recepient}
            return render(request, 'sending_receiving/success.html', context)
    
    context = {'form': form}
    return render(request, 'sending_receiving/send_file.html', context)
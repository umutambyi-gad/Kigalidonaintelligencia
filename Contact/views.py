from django.shortcuts import render, redirect
from django.core.mail import send_mail
from decouple import Csv, config


# Create your views here.
def contact(request):
    if request.method == 'POST':
        sender_firstname = request.POST['firstname']
        sender_lastname = request.POST['lastname']
        sender_names = f'{sender_firstname} {sender_lastname}'
        subject = request.POST['subject']
        sender_email = request.POST['email']
        message = request.POST['message']

        send_mail(subject, # subject
            f'{sender_names} sends {message}', # message
			sender_email, # from_email
			config('RECIEVER_EMAILS', cast=Csv())
        )
        return redirect('/contact')

    return render(request, 'contact.html')

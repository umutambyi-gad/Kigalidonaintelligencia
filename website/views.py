from django.shortcuts import render, redirect
from django.core.mail import send_mail


# Create your views here.
def home(request):
    return render(request, 'index.html')

def aboutUs(request):
    return render(request, 'about-us.html')

def books(request):
    return render(request, 'books.html')

def bookSingle(request, book_id, book_title_slug):
    return render(request, 'book-single.html')

def blogs(request):
    return render(request, 'blogs.html')

def blogSingle(request, blog_id, blog_title_slug):
    return render(request, 'blog-single.html')

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
			['umutambyig@gmail.com']
        )
        return redirect('/contact')

    return render(request, 'contact.html')

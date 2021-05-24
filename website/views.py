from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')

def books(request):
    return render(request, 'books.html')

def blogs(request):
    return render(request, 'blogs.html')

def contact(request):
    return render(request, 'contact.html')

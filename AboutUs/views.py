from django.shortcuts import render
from Home.models import TestimonyAdding
from .models import AboutUs
from Contact.views import footerContacts


# Create your views here.
def aboutUs(request):
    testinony_adding = TestimonyAdding.objects.all()
    About_us = AboutUs.objects.first()
    context = {
        'testimonies': testinony_adding,
        'about_us': About_us
    }
    context = {**context, **footerContacts(request)}
    return render(request, 'about-us.html', context=context)

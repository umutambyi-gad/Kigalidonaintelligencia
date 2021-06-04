from django.shortcuts import render
from Home.models import TestimonyAdding


# Create your views here.
def aboutUs(request):
    testinony_adding = TestimonyAdding.objects.all()
    context = {
        'testimonies': testinony_adding
    }
    return render(request, 'about-us.html', context=context)

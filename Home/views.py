from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from .models import (
    HomeBackground,
    HomeWelcoming,
    TestimonyAdding
)


# Create your views here.
def home(request):
    # Addition of testimonies
    if request.method == 'POST':
        author_names = request.POST['names']
        author_email = request.POST['email']
        author_image = request.FILES.get('image', None)
        author_testimony = request.POST['testimony']
        linkedin_profile = request.POST.get('linkedin', None)
        facebook_profile = request.POST.get('facebook', None)
        twitter_profile = request.POST.get('twitter', None)
        instagram_profile = request.POST.get('instagram', None)
        
        if author_image not in ('', None):
            TestimonyAdding.objects.create(
                author_names=author_names, 
                author_email=author_email,
                author_image=author_image,
                author_testimony=author_testimony,
                linkedin_profile=linkedin_profile,
                facebook_profile=facebook_profile,
                twitter_profile=twitter_profile,
                instagram_profile=instagram_profile
            )
        else:
            TestimonyAdding.objects.create(
                author_names=author_names, 
                author_email=author_email,
                author_testimony=author_testimony,
                linkedin_profile=linkedin_profile,
                facebook_profile=facebook_profile,
                twitter_profile=twitter_profile,
                instagram_profile=instagram_profile
            )
        
        redirect('/')
    
    home_background = HomeBackground.objects.all()
    home_welcoming = HomeWelcoming.objects.first()
    testinony_adding = TestimonyAdding.objects.all()
    context = {
        'home_background': home_background,
        'home_welcoming': home_welcoming,
        'testimonies': testinony_adding
    }
    return render(request, 'index.html', context=context)


def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(
                    username=username,
                    password=password
                )
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                return redirect('login/')
    
    return render(request, 'login.html')

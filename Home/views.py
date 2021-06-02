from django.shortcuts import redirect, render
from .models import TestimonyAdding


# Create your views here.
def home(request):
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

    return render(request, 'index.html')

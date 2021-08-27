from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.http import JsonResponse
from .models import (
    HomeBackground,
    HomeWelcoming,
    TestimonyAdding,
)
from Blogs.models import (
    Blogs,
    Categories as Blog_categories
)
from Books.models import (
    Books,
    Categories as Book_categories
)
from Contact.views import footerContacts


# Create your views here.
def home(request):
    # Addition of testimonies
    
    if request.is_ajax():
        author_names = request.POST['names']
        author_email = request.POST['email']
        author_image = request.FILES.get('image', None)
        author_testimony = request.POST['testimony']
        linkedin_profile = request.POST.get('linkedin', None)
        facebook_profile = request.POST.get('facebook', None)
        twitter_profile = request.POST.get('twitter', None)
        instagram_profile = request.POST.get('instagram', None)
        
        if author_image not in ('', None):
            new_testimony = TestimonyAdding.objects.create(
                author_name=author_names,
                author_email=author_email,
                author_image=author_image,
                testimony=author_testimony,
                linkedin_profile=linkedin_profile,
                facebook_profile=facebook_profile,
                twitter_profile=twitter_profile,
                instagram_profile=instagram_profile
            )

            return JsonResponse(
                {
                    'author': new_testimony.author_name,
                    'avatar': new_testimony.author_image.url,
                    'testimony': new_testimony.testimony,
                    'lnk_username': new_testimony.linkedin_profile,
                    'fb_username': new_testimony.facebook_profile,
                    'twt_username': new_testimony.twitter_profile,
                    'insta_username': new_testimony.instagram_profile
                }, status=200
            )
        else:
            new_testimony = TestimonyAdding.objects.create(
                author_name=author_names,
                author_email=author_email,
                testimony=author_testimony,
                linkedin_profile=linkedin_profile,
                facebook_profile=facebook_profile,
                twitter_profile=twitter_profile,
                instagram_profile=instagram_profile
            )
        
            return JsonResponse(
                {
                    'author': new_testimony.author_name,
                    'avatar': new_testimony.author_image.url,
                    'testimony': new_testimony.testimony,
                    'lnk_username': new_testimony.linkedin_profile,
                    'fb_username': new_testimony.facebook_profile,
                    'twt_username': new_testimony.twitter_profile,
                    'insta_username': new_testimony.instagram_profile
                }, status=200
            )
    
    home_background = HomeBackground.objects.all()
    home_welcoming = HomeWelcoming.objects.first()
    testinony_adding = TestimonyAdding.objects.all()
    blog_categories = Blog_categories.objects.all()
    book_categories = Book_categories.objects.all()
    recent_blogs = Blogs.recent_blogs()
    recent_books = Books.recent_books()
    context = {
        'home_background': home_background,
        'home_welcoming': home_welcoming,
        'testimonies': testinony_adding,
        'blog_categories': blog_categories,
        'book_categories': book_categories,
        'recent_blogs': recent_blogs,
        'recent_books': recent_books
    }
    context = {**context, **footerContacts(request)}
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
                return redirect('/')
    else:
        return redirect('/')
        
    context = {}
    context = {**context, **footerContacts(request)}
    return render(request, 'login.html', context=context)

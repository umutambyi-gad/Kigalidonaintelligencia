from django.urls import path
from . import views


app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs', views.blogs, name='blogs'),
    path('contact', views.contact, name='contact')
]

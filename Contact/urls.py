from django.urls import path
from . import views


app_name = 'Contact'

urlspattern = [
    path('contact', views.contact, name='contact')
]

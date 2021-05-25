
from django.urls import path
from . import views


app_name = 'About-us'

urlpatterns = [
    path('', views.aboutUs, name='aboutUs')
]

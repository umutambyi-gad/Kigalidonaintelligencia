from django.urls import path
from . import views


app_name = 'Home'

urlpatterns =[
    path('', views.home, name='home'),
    path('login/', views.login, name='login')
]

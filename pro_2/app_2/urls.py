from django.urls import path,include
from app_2 import views

urlpatterns = [
#    path('/a',views.help,name='help'),
    path('',views.User,name='help')
]
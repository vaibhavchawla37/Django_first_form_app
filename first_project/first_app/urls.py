# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path,include
from first_app import views

app_name = 'first_app_urls'

urlpatterns = [
    path('',views.relative,name='index'),
    path('form_1',views.forms_1,name='form_1'),
    path('form',views.forms,name='form'),
    path('form_2',views.model_form,name='form_2'),
    path('other',views.other,name='other'),
]


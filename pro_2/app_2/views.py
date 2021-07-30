from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index_first.html')

def User(request):
    return render(request,'index.html')

def Help(request):
    help_dict={'insert_me':'HELP PAGE',}
    return render(request,'index.html',context=help_dict)
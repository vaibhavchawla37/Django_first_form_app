from django.shortcuts import render
from .forms import Name_form,model_new_form
from first_app.models import  Topic,Webpage,Access_record,custom_form_modal
# Create your views here.

# def index(request):
#     my_dict={'insert_me':'Hello i am from views.py',}
#     return render(request,'first_app/index.html',context=my_dict)

def index(request):
    webpages_list = Access_record.objects.order_by('id')
    date_dict={'access_record':webpages_list}
    return render(request,'first_app/index.html',context=date_dict)

def other(request):
    return render(request,'first_app/other.html')

def relative(request):
     return render(request,'first_app/index._first.html')


def forms_1(request):
    if request.method =='POST':
        data = request.POST
        if(data['news']=='on'):
            temp = True
        else:
            temp=False
        print(data)
        t=custom_form_modal(name=data['name'],email=data['email'],news=temp,select_type=data['find-us'],text=data['message'])
        t.save()
    return render(request,'wb/index.html')

def forms(request):
    data = Name_form()
    
    if request.method =='POST':
        form = Name_form(request.POST)

        if form.is_valid():
            print(form.cleaned_data)


    data_form = {'form':data,}
    return render(request,'first_app/forms.html',context=data_form)

def model_form(request):
    data = model_new_form()
    print(1)
    if request.method =='POST':
        form = model_new_form(request.POST)
        print(2)
        if form.is_valid():
            print(3)
            form.save(commit=True)
            print(form.cleaned_data)
            

    data_form = {'form':data,}
    return render(request,'first_app/forms.html',context=data_form)



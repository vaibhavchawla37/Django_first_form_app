from django import forms
from django.forms import fields

from first_app.models import Webpage
from django.forms.widgets import PasswordInput, Textarea

BIRTH_YEAR_CHOICES = ['1980','2021']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Bluevgg'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class Name_form(forms.Form):
    name = forms.CharField(help_text='')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'jum'}))
    text = forms.CharField(widget=Textarea)
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=range(1980,2021)))
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )

class dummy(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    
    text = forms.CharField(widget=Textarea)
    

class model_new_form(forms.ModelForm):

    class Meta:
        model = Webpage
        fields = '__all__'
        widgets = { 'name' : forms.TextInput( attrs={'class' : 'jum gh'}),
                    'url': forms.URLInput(attrs={'class' : 'jum'}),
                    'topic': forms.Select(attrs={'class' : 'jum'})   } 
                    


        

    
    

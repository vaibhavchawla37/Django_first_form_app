from typing import Text
from django.db import models
from django.db.models.fields import TextField
from django.forms import widgets
#Create your models here
class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name

TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]
CHOICES = [
    ('friends', 'Friends.'),
    ('search engine', 'Search engine.'),
    ('add', 'Add.'),
]
class Webpage(models.Model):
    topic = models.ForeignKey(Topic ,on_delete=models.CASCADE)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self) :
        return self.name

class Access_record(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class custom_form_modal(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    select_type = models.CharField(max_length=20)    
    news = models.BooleanField()
    text = models.TextField()

    def __str__(self) :
        return self.name

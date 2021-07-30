import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','pro_2.settings')

import django
django.setup()

import random
from app_2.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for i in range(N):
        f_fname = fakegen.first_name()
        f_lname = fakegen.last_name()
        f_email = fakegen.email()
        User.objects.get_or_create(first_name=f_fname,last_name=f_lname,email=f_email)

if __name__ == '__main__':
    print('Populating Script ') 
    N = input('Enter number of data records:')
    populate(int(N))
    print('Completed population')

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django

django.setup()

#Fake population script

import random

from hello_world.models import User, Task
from faker import Faker

fakegen = Faker()

users = ['John Gammonn', 'Daniel Ford', 'Example Jones']

def add_user():
    t = User.objects.get_or_create(username=random.choice(users))[0]
    t.save()
    return t

def populate(n=10):
    for entry in range(n):
        top = add_user()

        fake_date = fakegen.date()
        fake_text = fakegen.text()

        # BECAUSE topic is a foreign key, its why we pass it in as t, which is a Topic.object
        task = Task.objects.get_or_create(username=top, task=fake_text, start_date=fake_date)[0]



if __name__ == '__main__':
    print("Populating Script!")
    populate(40)


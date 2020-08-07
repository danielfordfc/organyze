import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django

django.setup()


#Fake population script

import random

from hello_world.models import AccessRecords, Webpage, Topic
from faker import Faker

fakegen = Faker()

topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(n=10):
    for entry in range(n):
        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # BECAUSE topic is a foreign key, its why we pass it in as t, which is a Topic.object
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # BECAUSE webpg is a foreign key, its why we pass it in as webpg, which is a Webpage.object
        acc_rec = AccessRecords.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__ == '__main__':
    print("Populating Script!")
    populate(20)


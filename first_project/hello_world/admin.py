from django.contrib import admin
from hello_world.models import AccessRecords, Topic, Webpage, User, Task

# Register your models here.
admin.site.register(Topic)
admin.site.register(AccessRecords)
admin.site.register(Webpage)
admin.site.register(User)
admin.site.register(Task)

#Super User Details: daniel, email, 717!



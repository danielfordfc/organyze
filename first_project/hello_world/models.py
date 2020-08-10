from django.db import models

# Create your models here.

class Topic(models.Model):
    """
    Topic is a derived class from models.Model

    """
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name


class Webpage(models.Model):

    """
    ForeignKey() defines a many-to-one relationship between the tables.
    """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecords(models.Model):

    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class User(models.Model):

    username = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return str(self.username)


class Task(models.Model):

    username = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=5000, unique=True)
    start_date = models.DateField()

    def __str__(self):
        return str(str(self.start_date) + str(self.task))


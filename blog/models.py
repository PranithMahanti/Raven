from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    link= models.CharField(default='', max_length=100)
    post = models.TextField(max_length=2000)
    date = models.DateField("Published on: ")
    tags = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    link= models.CharField(default='', max_length=100)
    worked_with = models.CharField(default='', max_length=200)
    info = models.CharField(max_length=2000)
    date = models.DateField("Published on: ")

    def __str__(self):
        return self.title

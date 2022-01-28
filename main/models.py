from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    link_title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    data = models.TextField()
    date = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=100)
    content = models.TextField()
    date = models.CharField(max_length=20)

    def __str__(self):
        return self.name
from django.db import models


class Contact(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)


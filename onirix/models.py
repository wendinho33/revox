from django.db import models

# Create your models here.

class Contact_US(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email

class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Payments(models.Model):
    PRICE_LIST = [
        ('$38','$38'),
        ('$50','$50'),
    ]
    name = models.CharField(max_length=255)
    email = models.EmailField()
    price = models.CharField(max_length=3, choices=PRICE_LIST, default='')
    
    def __str__(self):
        return self.email
    
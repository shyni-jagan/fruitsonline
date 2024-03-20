from django.db import models
class product(models.Model):
    FirstName=models.CharField(max_length=100)
    Address=models.TextField()
    Gender=models.CharField(max_length=100)
    Email=models.EmailField()
    PhoneNumber=models.IntegerField()


# Create your models here.

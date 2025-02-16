from django.db import models

# Create your models here.

class ClubMember(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    date_of_birth = models.DateField()
    date_of_join = models.DateField()
from django.db import models

# Create your models here.
class job(models.Model):
    image= models.ImageField(upload_to='images/')
    summary = models.CharField(max_length= 200)
class blogs(models.Model):

    image= models.ImageField(upload_to='images/')
    summary = models.CharField(max_length= 200)
    body= models.CharField(max_length=200)
    pub_date= models.DateTimeField() 
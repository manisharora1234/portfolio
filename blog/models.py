from django.db import models

# Create your models here.
class Blog(models.Model):
    
    image= models.ImageField(upload_to='images/')
    summary = models.CharField(max_length= 200)
    body= models.CharField(max_length=200)
    pub_date= models.DateTimeField() 
    #def __str__(self):
       #

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
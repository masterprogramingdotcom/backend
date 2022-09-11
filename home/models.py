from django.db import models

# Create your models here.


class Enquire(models.Model):
    name = models.CharField(max_length=255, null=True,blank=True)
    email = models.EmailField(max_length=255, null=True,blank=True)
    number = models.CharField(max_length=255, null=True,blank=True)
    city = models.CharField(max_length=255, null=True,blank=True)
    program = models.CharField(max_length=255, null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.name
    


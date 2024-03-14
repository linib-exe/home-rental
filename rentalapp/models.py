from django.db import models

# Create your models here.
class Property(models.Model):
    title = models.CharField(max_length = 20)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images/',null=True,blank=True)

    def __str__(self):
        return self.title
    
class Profile(models.Model):
    firstname = models.CharField(max_length = 20)
    middlename = models.CharField(max_length = 20,blank=True,null=True)
    lastname = models.CharField(max_length = 20)
    username = models.CharField(max_length = 20)
    password1 = models.CharField(max_length = 20)
    password2 = models.CharField(max_length = 20)
    contact = models.CharField(max_length = 20)

    def __str__(self):
        return self.username


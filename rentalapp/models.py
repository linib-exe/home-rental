from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Property(models.Model):
    title = models.CharField(max_length = 20)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.title
    



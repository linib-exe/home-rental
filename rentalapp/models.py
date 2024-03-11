from django.db import models

# Create your models here.
class Property(models.Model):
    title = models.CharField(max_length = 20)
    description = models.TextField()
    price = models.FloatField()

    def __str__(property):
        return property.title

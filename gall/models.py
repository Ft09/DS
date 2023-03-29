from django.db import models

# Create your models here.

class Flower(models.Model):
    
    #title
    #image
    #description
    
    title = models.CharField(max_length=100)
    image = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
class Vegetable(models.Model):
    reciepe_name = models.CharField(max_length=100)
    reciepe_description = models.TextField()
    reciepe_image = models.ImageField(upload_to='images/')
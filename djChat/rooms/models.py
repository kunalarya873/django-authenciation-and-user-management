from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, auto_created=True)

    def __str__(self):
        return self.name
    
    def save(self):
        self.slug = self.name
        super().save()
        

from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age= models.PositiveIntegerField()
    father_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    category_name = models.CharField(max_length=100)

class Books(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=100)
    
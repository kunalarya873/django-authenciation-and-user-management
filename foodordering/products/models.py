from django.db import models
import uuid
# Create your models here.

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    product_slug = models.SlugField(unique=True)
    product_description = models.TextField()
    product_price = models.IntegerField(default=0)
    product_demo_price = models.IntegerField(default=0)
    

    def __str__(self):
        return self.name
class ProductMetaformation(BaseModel):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.CharField(null=True, blank=True)
    product_measuring = models.CharField(max_length=100, choices=(('KG', 'KG'), ('ML', 'ML'), ("L", "L")))
    product_weight = models.IntegerField(default=0)
    restrict_quantity = models.CharField(max_length=100)
    is_restrict =  models.BooleanField(default=False)

class ProductImages(BaseModel):
    product_images = models.ImageField(upload_to='images/')
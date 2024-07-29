from django.db import models
from django.core.validators import MinValueValidator
from django.utils.text import slugify

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self) -> str:
        return self.category_name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)

class QuantityVariant(models.Model):
    variant_name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.variant_name

class ColorVariant(models.Model):
    color_name = models.CharField(max_length=255, unique=True)
    color_code = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.color_name

class SizeVariant(models.Model):
    size_name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.size_name
    
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, editable=False)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to='static/products')
    price = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.TextField()
    stock = models.IntegerField(default=100, validators=[MinValueValidator(0)])
    quantity_type = models.ForeignKey(QuantityVariant, null=True, blank=True, on_delete=models.PROTECT, related_name='products')
    size_type = models.ForeignKey(SizeVariant, null=True, blank=True, on_delete=models.PROTECT, related_name='products')
    color_type = models.ForeignKey(ColorVariant, null=True, blank=True, on_delete=models.PROTECT, related_name='products')


    def __str__(self) -> str:
        return self.product_name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super().save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete= models.PROTECT)
    image = models.ImageField(upload_to='static/products')

from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(QuantityVariant)
admin.site.register(SizeVariant)
admin.site.register(ColorVariant)
admin.site.register(ProductImage)
from django.contrib import admin
from .models import Profile, Location
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Location)  # Register the Location model
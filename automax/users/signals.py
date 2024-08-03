from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Profile, Location
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Profile)
def create_profile_location(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'location'):
        profile_location = Location.objects.create(user=instance)
        instance.location = profile_location
        instance.save()

@receiver(pre_delete, sender=Profile)
def delete_profile_location(sender, instance, **kwargs):
    if instance.location:
        instance.location.delete()

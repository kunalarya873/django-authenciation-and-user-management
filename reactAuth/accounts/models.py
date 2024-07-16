from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
import uuid
from django.conf import settings
from .manager import UserManager

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12, unique=True)
    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=4, null=True, blank=True)
    email_verification_token = models.CharField(max_length=200, null=True, blank=True)
    forget_password_token = models.CharField(max_length=200, null=True, blank=True)

    UNIQUE_FIELD = 'email'
    REQUIRED_FIELD = []
    objects = UserManager()

    def __str__(self):
        return self.username
    
    def name(self):
        return self.first_name + " " + self.last_name

@receiver(post_save, sender=User)
def send_email_token(sender, instance, created, **kwargs):
    if created:
        try:
            subject = "Your email needs to be verified"
            message = f"Hi {instance.username}, click the link to verify your email: {instance.email_verification_token}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [instance.email]
            send_mail(subject, message, email_from, recipient_list)
        except Exception as e:
            print(e)

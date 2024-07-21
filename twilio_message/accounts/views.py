from django.shortcuts import render, redirect
from .models import *
from .mixins import MessageHandler
import random
from django.contrib.auth import login
# Create your views here.
def login_view(request):
    if request.method == "POST":
        phone_number = request.POST['phone_number']
        profile = Profile.objects.filter(phone_number= phone_number)
        if not profile.exists():
            return redirect('/register/')
        profile[0].otp = random.randint(1000, 9999)
        profile[0].save()
        MessageHandler(phone_number, profile[0].otp).send_otp_on_phone()
        return redirect(f'/otp/{profile[0].uid}')

def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        phone_number = request.POST['phone_number']
        user = User.objects.create(username = username)
        profile = Profile.objects.create(user = user, phone_number = phone_number)
        return redirect('/')

    return render(request, 'register.html')

def otp(request, uid):
    if request.method == 'POST':
        otp = request.POST['otp']
        profile = Profile.objects.get(uid = uid)
        if profile.otp == otp:
            login(request, profile.user)
            profile.is_phone_verified = True
            profile.save()
            return redirect('/')
        
    return render(request, 'otp.html')
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth import logout
# Create your views here.

# @login_required
def frontpage(request):
    return render(request, 'core/base.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontpage')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('frontpage')
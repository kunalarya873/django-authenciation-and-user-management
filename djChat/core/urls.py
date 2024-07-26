from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", frontpage, name="frontpage"),
    path('signup/', signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name='core/login.html'), name="login"),
    path('logout/', custom_logout, name='logout'),  # Ensure the next_page is set
]
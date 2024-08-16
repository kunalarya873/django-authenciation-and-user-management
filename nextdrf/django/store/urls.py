from django.urls import path
from .views import *
app_name = "store"


urlpatterns = [
        path("api/", ProductListView.as_view(), name="store_home"),

]
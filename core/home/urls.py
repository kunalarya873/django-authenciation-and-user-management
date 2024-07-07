from django.urls import include, path
from .views import *
urlpatterns = [
    path('', home),
    path('post/', post_student),
    path('update-student/<int:id>/', update_student),
    path('delete-student/<int:id>/', delete_student)
]

from django.urls import path
from .views import *
urlpatterns = [
    path('student/', StudentAPI.as_view()),
    path('student/<int:id>/', StudentAPI.as_view(), name='student-api-detail'),
    path('register/', RegisterUser.as_view(), name='register_user'),
    path('generic-student/', StudentGeneric.as_view()),
    path('generic-student/<id>/', StudentGeneric1.as_view())
]   
'''path('post/', post_student),
    path('update-student/<int:id>/', update_student),
    path('delete-student/<int:id>/', delete_student),
    path('get-book/', get_book)'''
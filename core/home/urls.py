from django.urls import include, path
from .views import *
urlpatterns = [
    path('student/', StudentAPI.as_view()),
    path('student/<int:id>/', StudentAPI.as_view(), name='student-api-detail'),
]   
'''path('post/', post_student),
    path('update-student/<int:id>/', update_student),
    path('delete-student/<int:id>/', delete_student),
    path('get-book/', get_book)'''
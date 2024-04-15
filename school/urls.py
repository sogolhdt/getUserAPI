from django.urls import path
from . import views
urlpatterns = [
    path('students/', views.get_students_list, name = 'get_students_list'),
    path('add-student/', views.add_student, name = 'add_student'),
    path('get-student/', views.get_student_by_name, name = 'get_student'),
]

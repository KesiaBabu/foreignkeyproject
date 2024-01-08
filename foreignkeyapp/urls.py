from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('course',views.course,name='course'),
    path('student',views.student,name='student'),
    path('show',views.show,name='show'),
    path('add_course',views.add_course,name='add_course'),
    path('add_student',views.add_student,name='add_student'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('editdb/<int:pk>',views.editdb,name='editdb'),
    path('delete/<int:pk>',views.delete,name='delete'),
  
]
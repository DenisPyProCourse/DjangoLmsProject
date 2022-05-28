from django.urls import path

from .views import create_student
from .views import delete_student
from .views import get_students
from .views import update_student

# CRUD - Create, Read, Update, Delete

app_name = 'students'

urlpatterns = [
    path('', get_students, name='list'),                              # Read
    path('create/', create_student, name='create'),                   # Create
    path('update/<int:pk>/', update_student, name='update'),          # Update
    path('delete/<int:pk>/', delete_student, name='delete'),          # Delete
 ]
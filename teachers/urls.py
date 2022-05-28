from django.urls import path

from .views import get_teacher
from .views import generate_teachers
from .views import create_teacher
from .views import update_teacher
from .views import delete_teacher

app_name = 'teachers'

urlpatterns = [
    path('', get_teacher, name = 'list'),  # Read
    path('generate_teachers/', generate_teachers, name='generate'), #Generate
    path('create/', create_teacher, name='create'),            # Create
    path('update/<int:pk>', update_teacher, name='update'),           # Update
    path('delete/<int:pk>', delete_teacher, name='delete'),           # Delete
]
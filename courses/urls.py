from django.urls import path

from .views import create_course
from .views import delete_course
from .views import get_course
from .views import update_course


# CRUD - Create, Read, Update, Delete

app_name = 'courses'

urlpatterns = [
    path('', get_course, name='list'),  # Read
    path('create/', create_course, name='create'),            # Create
    path('update/<int:pk>', update_course, name='update'),           # Update
    path('delete/<int:pk>', delete_course, name='delete'),           # Delete
]

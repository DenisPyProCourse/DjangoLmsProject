from django.urls import path

from .views import create_group
from .views import delete_group
from .views import get_group
from .views import update_group


# CRUD - Create, Read, Update, Delete

app_name = 'groups'

urlpatterns = [
    path('', get_group, name='list'),  # Read
    path('create/', create_group, name='create'),            # Create
    path('update/<int:pk>', update_group, name='update'),           # Update
    path('delete/<int:pk>', delete_group, name='delete'),           # Delete
]

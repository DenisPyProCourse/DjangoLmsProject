from django.urls import path

from .views import CreateTeacherView
from .views import DeleteTeacherView
from .views import generate_teachers
from .views import ListTeacherView
from .views import UpdateTeacherView


app_name = 'teachers'

urlpatterns = [
    path('', ListTeacherView.as_view(), name='list'),                              # Read
    path('generate_teachers/', generate_teachers, name='generate'),   # Generate
    path('create/', CreateTeacherView.as_view(), name='create'),                   # Create
    path('update/<int:pk>', UpdateTeacherView.as_view(), name='update'),           # Update
    path('delete/<int:pk>', DeleteTeacherView.as_view(), name='delete'),           # Delete
]

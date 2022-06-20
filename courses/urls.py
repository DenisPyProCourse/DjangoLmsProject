from django.urls import path

from .views import CreateCourseView
from .views import DeleteCourseView
from .views import ListCoursesView
from .views import UpdateCourseView


# CRUD - Create, Read, Update, Delete

app_name = 'courses'

urlpatterns = [
    path('', ListCoursesView.as_view(), name='list'),                             # Read
    path('create/', CreateCourseView.as_view(), name='create'),                   # Create
    path('update/<int:pk>', UpdateCourseView.as_view(), name='update'),           # Update
    path('delete/<int:pk>', DeleteCourseView.as_view(), name='delete'),           # Delete
]

"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from teachers.views import get_teacher, generate_teachers, update_teacher, delete_teacher
from students.views import create_student
from students.views import get_students
from students.views import index
from students.views import update_student
from teachers.views import create_teacher
from groups.views import create_group, update_group, delete_group
from groups.views import get_group


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('teachers/', get_teacher, name = 'teachers'),                 # Read Teacher
    path('generate_teachers/', generate_teachers),  # Generate Teachers
    path('students/', get_students, name = 'students'),                # Read Student
    path('groups/', get_group, name = 'groups'),                     # Read Groups
    path('teachers/create/', create_teacher),          # Create Teacher
    path('students/create/', create_student),       # Create Student
    path('groups/create/', create_group),            # Create Group
    path('students/update/<int:pk>/', update_student),       # Update Student
    path('teachers/update/<int:pk>/', update_teacher),       # Update Teacher
    path('groups/update/<int:pk>', update_group),           # Update Group
    path('teachers/delete/<int:pk>', delete_teacher),           # Delete Teacher
    path('groups/delete/<int:pk>', delete_group),           # Delete Group

]

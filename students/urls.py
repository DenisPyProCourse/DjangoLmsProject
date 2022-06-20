from django.urls import path

# from .views import create_student
# from .views import delete_student
# from .views import get_students
# from .views import update_student
# from .views import UpdateStudent
from .views import CreateStudentView
from .views import DeleteStudentView
from .views import ListStudentView
from .views import UpdateStudentView

# CRUD - Create, Read, Update, Delete

app_name = 'students'

urlpatterns = [
    # path('', get_students, name='list'),                                     # Read
    path('', ListStudentView.as_view(), name='list'),                                     # Read
    # path('create/', create_student, name='create'),                          # Create
    path('create/', CreateStudentView.as_view(), name='create'),                          # Create
    # path('update/<int:pk>/', update_student, name='update'),          # Update
    # path('update/<int:pk>/', UpdateStudent.update, name='update'),      # Update
    path('update/<int:identity>/', UpdateStudentView.as_view(), name='update'),            # Update
    # path('delete/<int:pk>/', delete_student, name='delete'),                 # Delete
    path('delete/<int:pk>/', DeleteStudentView.as_view(), name='delete'),                 # Delete
 ]

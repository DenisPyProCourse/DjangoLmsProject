from django.urls import path

# from .views import create_group
# from .views import delete_group
# from .views import get_group
# from .views import update_group
from .views import CreateGroupView
from .views import DeleteGroupView
from .views import ListGroupView
from .views import UpdateGroupView

# CRUD - Create, Read, Update, Delete

app_name = 'groups'

urlpatterns = [
    # path('', get_group, name='list'),                               # Read
    path('', ListGroupView.as_view(), name='list'),                              # Read
    # path('create/', create_group, name='create'),                   # Create
    path('create/', CreateGroupView.as_view(), name='create'),                   # Create
    # path('update/<int:pk>', update_group, name='update'),           # Update
    path('update/<int:pk>', UpdateGroupView.as_view(), name='update'),           # Update
    # path('delete/<int:pk>', delete_group, name='delete'),            # Delete
    path('delete/<int:pk>', DeleteGroupView.as_view(), name='delete'),           # Delete
]

from django.urls import path
from .views import *
app_name='myapp'
urlpatterns = [
    path('hello/',hello,name='hello'),
    path('new_user/',new_user,name='new_user'),
    path('users/',allUsers,name='users'),
    path('users/<int:id>/',singleUser,name='singleUser')
]

from django.urls import path
from .views import *


urlpatterns = [
    path('', TaskList.as_view(), name='tasklist'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
]
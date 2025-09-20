from django.urls import path
from .views import (
    TaskListView,
    TaskCreate,
    DeleteView,
    TaskComplete,
    TaskUpdate
)


app_name = 'todo'


urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreate.as_view(), name='task_create'),
    path("update/<int:pk>/", TaskUpdate.as_view(), name="task_update"),
    path("complete/<int:pk>/", TaskComplete.as_view(), name="task_complete"),
    path("delete/<int:pk>/", DeleteView.as_view(), name="task_delete"),
]

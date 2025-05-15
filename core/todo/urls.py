from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('cbv-index/', views.IndexView.as_view(), name='index'),
    path('post/create/', views.TaskCreateView.as_view(), name='post-create'),

]
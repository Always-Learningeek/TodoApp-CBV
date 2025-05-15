from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import Task


class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

class TaskCreateView(CreateView):
    model = Task
    fields = ['title']


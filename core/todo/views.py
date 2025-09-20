from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView
)
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm
from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

class TaskListView(ListView, LoginRequiredMixin):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tasks'


class TaskCreate(CreateView, LoginRequiredMixin):
    model = Task
    fields = ["title"]
    success_url = reverse_lazy("todo:task_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)



class DeleteView(DeleteView, LoginRequiredMixin):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("todo:task_list")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        # بدون نمایش صفحه تایید، رکورد را حذف می‌کنیم
        task = self.get_object()
        task.delete()  # حذف رکورد از دیتابیس
        return redirect(self.success_url)


class TaskUpdate(UpdateView, LoginRequiredMixin):
    model = Task
    success_url = reverse_lazy("todo:task_list")
    form_class = TaskForm

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('todo:task_list')


class TaskComplete(View, LoginRequiredMixin):
    model = Task
    success_url = reverse_lazy("todo:task_list")
    ''' 
    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        object.done = True
        object.save()
        return redirect(self.success_url)
    '''
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs.get("pk"), user=request.user)
        task.done = True
        task.save()
        return redirect(self.success_url)

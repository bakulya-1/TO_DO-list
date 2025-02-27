from django.shortcuts import render
import random
from django.views.generic import ListView
from .models import Task, Category
from django.db.models import Q
from django import forms
from django.views.generic import DetailView, CreateView

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = Task.objects.all()
        category_filter = self.request.GET.get('category')
        search_query = self.request.GET.get('search')

        if category_filter:
            queryset = queryset.filter(category__id=category_filter)

        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query))

        return queryset

    def get_context_data(self):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        return context



class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'




class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category']

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = '/tasks/'




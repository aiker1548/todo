from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Tasks, Labels
from django.views import generic
from .forms import RegistrationForm, TaskCreateForm, LabelCreateForm, TaskUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
from transliterate import translit
from django.contrib import messages

def home_view(request):
    return render(request, 'todo/homePage.html')


class RegisterView(generic.FormView):
    form_class = RegistrationForm
    template_name = 'todo/register.html'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return redirect('home')


class LoginView(generic.FormView):
    form_class = AuthenticationForm
    template_name = 'todo/login.html'
    success_url = 'home'

    def form_valid(self, form):
        # Вызываем метод login, чтобы аутентифицировать пользователя
        login(self.request, form.get_user())
        return redirect(self.success_url)

    def get_success_url(self):
        return redirect(self.success_url)

    

def userLogout(request):
    logout(request)
    return redirect('home')


class UsersListView(generic.ListView):
    model = User
    context_object_name = 'users'
    allow_empty = True
    template_name = 'todo/usersList.html'

    def get_context_data(self, **kwargs) -> dict[str, any]:
        user_menu = menu.copy()
        context = super().get_context_data(**kwargs)
        context['menu'] = user_menu
        return context

class LabelsListView(generic.ListView):
    model = Labels
    context_object_name = 'labels'
    allow_empty = True
    template_name = 'todo/labelsList.html'

    def get_context_data(self, **kwargs) -> dict[str, any]:
        user_menu = menu.copy()
        context = super().get_context_data(**kwargs)
        context['menu'] = user_menu
        return context
    

class TasksListView(generic.ListView):
    model = Tasks
    context_object_name = 'tasks'
    allow_empty = True
    template_name = 'todo/tasksList.html'

    def get_context_data(self, **kwargs) -> dict[str, any]:
        user_menu = menu.copy()
        context = super().get_context_data(**kwargs)
        context['menu'] = user_menu
        return context
    



class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = TaskCreateForm
    template_name = 'todo/add_task.html'
    login_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        user_menu = menu.copy()
        context = super().get_context_data(**kwargs)
        context['menu'] = user_menu
        return context

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            try:
                existing_task = Tasks.objects.get(title=form.cleaned_data['title'], user=request.user)
                # Задача с похожим названием уже существует
                form.add_error('title', 'Задача с таким названием уже существует.')
                return render(request, self.template_name, {'form': form})
            except Tasks.DoesNotExist:
                # Задачи с таким названием нет, создаем новую
                task = form.save(commit=False)
                task.user = request.user
                slug = translit(task.title, 'ru', reversed=True)
                slug = slug.replace(' ', '_') + '_' +task.user.username
                task.slug = slug
                task.save()
                messages.success(request, 'Задача успешно создана.')
                return redirect('home')
        else:
            return render(request, self.template_name, {'form': form})
        

class LabelCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = LabelCreateForm
    template_name = 'todo/add_label.html'
    login_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        user_menu = menu.copy()
        context = super().get_context_data(**kwargs)
        context['menu'] = user_menu
        return context

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            try:
                existing_label = Labels.objects.get(label_name=form.cleaned_data['label_name'], user=request.user)
                # Метка с похожим названием уже существует
                form.add_error('label_name', 'Метка с таким названием уже существует.')
                return render(request, self.template_name, {'form': form})
            except Labels.DoesNotExist:
                # Метка с таким названием нет, создаем новую
                label = form.save(commit=False)
                label.user = request.user
                slug = translit(label.label_name, 'ru', reversed=True)
                slug = slug.replace(' ', '_') + '_' +label.user.username
                label.slug = slug
                label.save()
                messages.success(request, 'Метка успешно создана.')
                return redirect('home')
        else:
            return render(request, self.template_name, {'form': form})
   

class ShowTaskView(generic.DetailView):
    model = Tasks
    template_name = 'todo/showTask.html'
    slug_url_kwarg = 'task_slug'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        user_menu = menu.copy()
        context = super().get_context_data(**kwargs)
        context['menu'] = user_menu
        return context
    
class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tasks
    form_class = TaskUpdateForm
    template_name = 'todo/update_task.html'
    login_url = reverse_lazy('home')
    slug_url_kwarg = 'task_slug'

    def get_context_data(self, **kwargs):
        user_menu = menu.copy()  # Если у вас есть меню, добавьте его сюда
        context = super().get_context_data(**kwargs)
        context['menu'] = user_menu
        return context

    def get_success_url(self):
        return reverse_lazy('home')
    
# class TaskUpdateView(LoginRequiredMixin, DataMixin, UpdateView):
#     model = Tasks
#     form_class = TaskUpdateForm
#     template_name = 'todo/TaskUpdate.html'
#     success_url = reverse_lazy('home')
#     login_url = reverse_lazy('login')
#     slug_url_kwarg = 'task_slug'

#     def dispatch(self, request, *args, **kwargs):
#         task = self.get_object()
#         if task.user_id != self.request.user.pk:
#             return redirect('home')
#         return super().dispatch(request, *args, **kwargs)

#     def form_valid(self, form):
#         task = form.save()
#         task.user = self.request.user
#         task.save()
#         return redirect('task', task_slug=task.slug)



# class LabelUpdateView(LoginRequiredMixin, DataMixin, UpdateView):
#     model = Labels
#     form_class = LabelUpdateForm
#     template_name = 'todo/labelUpdate.html'
#     success_url = reverse_lazy('home')
#     login_url = reverse_lazy('login')
#     slug_url_kwarg = 'label_slug'

#     def dispatch(self, request, *args, **kwargs):
#         post = self.get_object()
#         if post.user_id != self.request.user.pk:
#             return redirect('home')
#         return super().dispatch(request, *args, **kwargs)

#     def form_valid(self, form):
#         label = form.save()
#         label.user = self.request.user
#         label.save()
#         return redirect('label', label_slug=label.slug)

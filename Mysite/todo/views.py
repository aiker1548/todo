from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task, State
from django.views import generic
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

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
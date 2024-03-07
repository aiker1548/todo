from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task, State
from django.views import generic
from .forms import RegistrationForm
from django.contrib.auth.models import User


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
    form_class = LoginForm
    template_name = 'todo/login.html'

    def form_valid(self, form: Any) -> HttpResponse:
        if 
        return super().form_valid(form)
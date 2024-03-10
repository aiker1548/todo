from django.urls import path
from django.urls import include
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', userLogout, name='logout'),
    
    path('users/', UsersListView.as_view(),name = 'users'),
    
    path('tasks/', TasksListView.as_view(),name = 'tasks'),
    path('tasks/create/', TaskCreateView.as_view(),name = 'tasksCreate'),
    path('tasks/<slug:task_slug>/', ShowTaskView.as_view(),name = 'showTask'),
    path('tasks/<slug:task_slug>/update/', TaskUpdateView.as_view(),name = 'taskUpdate'),

    path('labels/', LabelsListView.as_view(),name = 'labels'),
    path('labels/create/', LabelCreateView.as_view(),name = 'labelCreate'),
]

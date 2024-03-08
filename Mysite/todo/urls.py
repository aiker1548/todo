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
    #path('tasks/<slug: task_slug>/', TaskDiteilView.as_view(),name = 'task'),
    #path('tasks/<slug: task_slug>/update/', TaskUpdateView.as_view(),name = 'taskUpdate'),
    path('tasks/create/', TaskCreateView.as_view(),name = 'tasksCreate'),
    
    path('labels/', LabelsListView.as_view(),name = 'labels'),
    #path('labels/<slug: label_slug>/update/', LabelUpdateView.as_view(),name = 'labelUpdate'),
    #path('labels/create/', LabelCreateView.as_view(),name = 'labelCreate'),
]
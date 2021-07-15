"""event_scheduler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from users import views as user_views
from django.contrib.auth import views as auth_views
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('tasks.urls')),
    path('register/',user_views.register, name='register'),
    path('profile/',user_views.profile, name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('accounts/', include('allauth.urls')),
    path('alltask/<int:pk>/',views.TASKSEE),
    # path("createtask/",views.CREATETASK),
    path('API/', views.TaskListAPI.as_view(), name='tasks-list'),
    path('API/<int:pk>/', views.TaskDetailAPI.as_view(), name='tasks-detail'),
    path('API/new/', views.TaskCreateAPI.as_view(), name='tasks-create'),

    path('BTAPI/', views.BTTaskListAPI.as_view(), name='tasks-list'),
    path('BTAPI/<int:pk>/', views.BTTaskDetailAPI.as_view(), name='tasks-detail'),
    path('BTAPI/new/', views.BTTaskCreateAPI.as_view(), name='tasks-create'),

]

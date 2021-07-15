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

    path('CHAPI/', views.CHTaskListAPI.as_view(), name='tasks-list'),
    path('CHAPI/<int:pk>/', views.CHTaskDetailAPI.as_view(), name='tasks-detail'),
    path('CHAPI/new/', views.CHTaskCreateAPI.as_view(), name='tasks-create'),

    path('CLAPI/', views.CLTaskListAPI.as_view(), name='tasks-list'),
    path('CLAPI/<int:pk>/', views.CLTaskDetailAPI.as_view(), name='tasks-detail'),
    path('CLAPI/new/', views.CLTaskCreateAPI.as_view(), name='tasks-create'),

    path('CEAPI/', views.CETaskListAPI.as_view(), name='tasks-list'),
    path('CEAPI/<int:pk>/', views.CETaskDetailAPI.as_view(), name='tasks-detail'),
    path('CEAPI/new/', views.CETaskCreateAPI.as_view(), name='tasks-create'),

    path('CSEAPI/', views.CSETaskListAPI.as_view(), name='tasks-list'),
    path('CSEAPI/<int:pk>/', views.CSETaskDetailAPI.as_view(), name='tasks-detail'),
    path('CSEAPI/new/', views.CSETaskCreateAPI.as_view(), name='tasks-create'),

    path('DESAPI/', views.DESTaskListAPI.as_view(), name='tasks-list'),
    path('DESAPI/<int:pk>/', views.DESTaskDetailAPI.as_view(), name='tasks-detail'),
    path('DESAPI/new/', views.DESTaskCreateAPI.as_view(), name='tasks-create'),

    path('ECEAPI/', views.ECETaskListAPI.as_view(), name='tasks-list'),
    path('ECEAPI/<int:pk>/', views.ECETaskDetailAPI.as_view(), name='tasks-detail'),
    path('ECEAPI/new/', views.ECETaskCreateAPI.as_view(), name='tasks-create'),

    path('EEEAPI/', views.EEETaskListAPI.as_view(), name='tasks-list'),
    path('EEEAPI/<int:pk>/', views.EEETaskDetailAPI.as_view(), name='tasks-detail'),
    path('EEEPI/new/', views.EEETaskCreateAPI.as_view(), name='tasks-create'),

    path('MAAPI/', views.MATaskListAPI.as_view(), name='tasks-list'),
    path('MAAPI/<int:pk>/', views.MATaskDetailAPI.as_view(), name='tasks-detail'),
    path('MAAPI/new/', views.MATaskCreateAPI.as_view(), name='tasks-create'),

    path('MEAPI/', views.METaskListAPI.as_view(), name='tasks-list'),
    path('MEAPI/<int:pk>/', views.METaskDetailAPI.as_view(), name='tasks-detail'),
    path('MEAPI/new/', views.METaskCreateAPI.as_view(), name='tasks-create'),

    path('PHAPI/', views.PHTaskListAPI.as_view(), name='tasks-list'),
    path('PHAPI/<int:pk>/', views.PHTaskDetailAPI.as_view(), name='tasks-detail'),
    path('PHAPI/new/', views.PHTaskCreateAPI.as_view(), name='tasks-create'),

]

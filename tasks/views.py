from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.template.defaulttags import csrf_token
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task
# from .serializer import TaskSerializer
import io
from rest_framework.parsers import JSONParser
# from .serializer import TaskDSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import CreateModelMixin

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Task
from .models import BT
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .aserializer import TaskSerializer
from .serializer import BTSerializer
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework import generics, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
import django_filters.rest_framework

# Create your views here.
def index(request):
    param = {
        'tasks': Task.objects.all()
    }
    return render(request, 'tasks/index.html', param)


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    ordering = ['date']


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'event_type', 'target_batch', 'target_branch', 'date', 'time_from', 'time_to', 'remainder',
              'remainder_date', 'remainder_time', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'event_type', 'target_batch', 'target_branch', 'date', 'time_from', 'time_to', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.author:
            return True
        return False


class TaskDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Task
    success_url = '/'

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.author:
            return True
        return False


def TASKSEE(request, pk):
    stu = Task.objects.get(id=pk)
    serializer = TaskSerializer(stu)
    # json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)




# @csrf_exempt
# def CREATETASK(request):
#     if request.method == "POST":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#
#         pythondata = JSONParser().parse(stream)
#
#         serializer = TaskDSerializer(data=pythondata)
#
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'created'}
#             json_data = JSONRenderer().render(res)
#
#             return HttpResponse(json_data, content_type='application/json')
#     json_data = JSONRenderer().render(serializer.errors)
#     return HttpResponse(json_data, content_type='application/json')





class TaskListAPI(generics.ListAPIView):

    serializer_class = TaskSerializer
    permission_class=(permissions.IsAuthenticatedOrReadOnly,)
    queryset = Task.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title','description','author__name')


class TaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_class=(permissions.IsAuthenticatedOrReadOnly,)



class TaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_class=(permissions.IsAuthenticatedOrReadOnly,)


    def post(self, request):
        return self.create(request)


class BTTaskListAPI(generics.ListAPIView):

    serializer_class = BTSerializer
    permission_class=(permissions.IsAuthenticatedOrReadOnly,)
    queryset = BT.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title','description','author__name')


class BTTaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BTSerializer
    queryset = BT.objects.all()
    permission_class=(permissions.IsAuthenticatedOrReadOnly,)



class BTTaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = BTSerializer
    queryset = BT.objects.all()
    permission_class=(permissions.IsAuthenticatedOrReadOnly,)


    def post(self, request):
        return self.create(request)

def task(request):
    return render(request,'tasks/TaskView.html')
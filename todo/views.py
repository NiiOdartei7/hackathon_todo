# Create your views here.
from urllib import response
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
# from .serializers import TodoListSerializer
from .models import Todo
# from .models import ToDoList
from django.db.models import Count
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound
import os


# Create your views here.
# class TodoListView(viewsets.ModelViewSet):
#     serializer_class = TodoListSerializer
#     queryset = ToDoList.objects.all()

    # def list(self):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     result_list = list(queryset.values('tasks').annotate(count=Count('tasks')))
    #     return result_list


    # def get_queryset(self):
    #     return ToDoList.objects.annotate(Count('id'))
        
        # return ToDoList.objects.annotate(total_tasks=Count('tasks'))

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    
class Assets(View):

    def get(self, _request, filename):
        path = os.path.join(os.path.dirname(__file__), 'static', filename)

        if os.path.isfile(path):
            with open(path, 'rb') as file:
                return HttpResponse(file.read(), content_type='application/javascript')
        else:
            return HttpResponseNotFound()




   





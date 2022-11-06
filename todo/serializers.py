from rest_framework import serializers
from .models import Todo
# from .models import ToDoList
# from .models import Metrics
# class TodoListSerializer(serializers.ModelSerializer):
    
#     # total_tasks = serializers.SerializerMethodField
    
#     class Meta:
#         model = ToDoList
#         fields = ('id', 'title')

    # def numberofTasks(self,obj):
    #     count = obj.total_tasks.count()
    #     return count

    

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed','created_date','due_date')

# class MetricSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Metrics
#         fields = ('id','NumberOfTasks', 'NumberofCompTasks', 'NumberOfNonCompTasks')


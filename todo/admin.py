from django.contrib import admin
from .models import Todo
# from .models import ToDoList
# from .models import Metrics

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'created_date', 'due_date' )

# class ToDoListAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'tasks')

# class MetricsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'NumberOfTasks', 'NumberOfCompTasks', 'NumberofNonCompTasks' )
# Register your models here.

admin.site.register(Todo, TodoAdmin)
# admin.site.register(ToDoList, ToDoListAdmin)
# admin.site.register(Metrics, MetricsAdmin)
# Register your models here.
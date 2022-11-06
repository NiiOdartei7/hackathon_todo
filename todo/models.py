from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils import dateformat




# Create your models here.


# def one_week_hence():
#     return timezone.now() + timezone.timedelta(days=7)

# class ToDoList(models.Model):
#     title = models.CharField(max_length=100, unique=True)

#     # task_count = models.IntegerField()
   
#     # def numberofTasks(self):
#     #     return self.tasks.count()
    
#     def get_absolute_url(self):
#         return reverse("list", args=[self.id])

#     def __str__(self):
#         return self.title

    


class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    # todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name = 'tasks')

    def _str_(self):
        return self.title


# Task_count = Todo.objects.count()


# class Metrics(models.Model):
#     NumberOfTasks = models.IntegerField(Task_count)
#     NumberOfCompTasks = models.IntegerField(Todo.objects.filter(completed = True))
#     NumberofNonCompTasks = models.IntegerField(Todo.objects.filter(completed = False))
#     todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
#     todo = models.ForeignKey(Todo, on_delete = models.CASCADE)



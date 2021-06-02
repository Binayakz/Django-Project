from django.db import models


class Todo(models.Model):
    
    tasks = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.tasks

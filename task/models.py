from django.db import models
from django.utils import timezone

def default_to_one_week():
    return timezone.now() + timezone.timedelta(days=7)

class Category(models.Model):
    title = models.CharField(max_length=30, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
        
    class Meta:
        indexes = [models.Index(fields=['title'])]
        ordering = ('-created',)


class Task(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    rating = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(default=default_to_one_week)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks')
    
    def __str__(self):
        return self.title
        
    class Meta:
        indexes = [models.Index(fields=['-due_date', '-created'])]
        ordering = ('-due_date',)
        
        
        
        
        
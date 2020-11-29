from django.db import models

# Create your models here.
class Event(models.Model):
    eventName = models.CharField(max_length=200,blank=True)
    deptName = models.CharField(max_length=200,blank=True)
    desc = models.TextField(max_length=200,blank=True)
    rules = models.TextField(max_length=200,blank=True)
    def __str__(self):
        return self.eventName+f" ({self.deptName})"
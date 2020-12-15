from django.db import models

# Create your models here.

class DepartmentEventIsland(models.Model):
    eventName = models.CharField(max_length=200,blank=True)
    deptslug = models.CharField(max_length=200,blank=True)
    deptid = models.CharField(max_length=200,blank=True)
    def __str__(self):
        return f"{self.eventName} - {self.deptslug} ({self.deptid})"
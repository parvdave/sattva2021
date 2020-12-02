from django.db import models

# Create your models here.
class Event(models.Model):
    eventName = models.CharField(max_length=200,blank=True)
    deptName = models.CharField(max_length=200,blank=True)
    desc = models.TextField(max_length=200,blank=True)
    rules = models.TextField(max_length=200,blank=True)
    content = models.CharField(max_length=1000,blank=True)
    def __str__(self):
        return self.eventName+f" ({self.deptName})"
class SoloSinging(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phoneNum = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = "Solo Singing Users"
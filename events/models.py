from django.db import models

# Create your models here.
class Event(models.Model):
    eventslug = models.CharField(max_length=200,blank=True)
    eventType = models.CharField(max_length=200,blank=True)
    eventName = models.CharField(max_length=200,blank=True)
    deptName = models.CharField(max_length=200,blank=True)
    desc = models.TextField(max_length=1000,blank=True)
    rules = models.TextField(max_length=1000,blank=True)
    content = models.TextField(max_length=1000,blank=True)
    url = models.TextField(max_length=200,blank=True)
    def __str__(self):
        return self.eventName+f" ({self.deptName})"


class SoloSinging(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phoneNum = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = "Solo PA Form"


class GroupEventPA(models.Model):
    name = models.CharField(max_length=200,blank=True)
    email = models.EmailField(max_length=200,blank=True)
    phoneNum = models.CharField(max_length=200,blank=True)
    college = models.CharField(max_length=200,blank=True)
    groupname = models.CharField(max_length=200,blank=True)
    class Meta:
        verbose_name_plural = "Group PA Form"

class Poetry(models.Model):
    name = models.CharField(max_length=200,blank=True)
    age = models.IntegerField(default=2,max_length=100)
    email = models.EmailField(max_length=200,blank=True)
    address = models.TextField(max_length=300,blank=True)
    phoneNum = models.CharField(blank=True,max_length=10)
    whatsapp = models.CharField(max_length=10,blank=True)
    contacted = models.BooleanField(default=False,blank=True)

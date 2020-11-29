from django.db import models

# Create your models here.
class Member(models.Model):
    firstName = models.CharField(max_length=200,blank=True)
    lastName = models.CharField(max_length=200,blank=True)
    stream = models.CharField(max_length=200,blank=True)
    course = models.CharField(max_length=200,blank=True)
    year = models.CharField(max_length=200,blank=True)
    position = models.CharField(max_length=200,blank=True)
    deptName = models.CharField(max_length=200,blank=True)
    img = models.ImageField(upload_to='corepics',blank=True)
    quote = models.TextField(max_length=400,blank=True)
    def __str__(self):
        return self.firstName+ ' ' + self.lastName + f' ({self.deptName})'
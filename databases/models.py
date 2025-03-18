from django.db import models

# Create your models here.

class student(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField(max_length=50)
  phone = models.CharField(max_length=15)
  address = models.TextField()
  
  def __str__(self):
    return self.first_name


class teacher(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField(max_length=50)
  phone = models.CharField(max_length=15)
  address = models.TextField()
  student = models.ManyToManyField('student', related_name='teachers')
  
  def __str__(self):
    return self.first_name
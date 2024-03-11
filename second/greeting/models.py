from django.db import models

# Create your models here.
class add_details(models.Model):
    taskid=models.CharField(max_length=30)
    taskname=models.CharField(max_length=15)
    projectname=models.CharField(max_length=30)
    description=models.CharField(max_length=50)
    start_time = models.DateField()
    end_time = models.DateField()
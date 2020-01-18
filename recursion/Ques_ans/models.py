from django.db import models

# Create your models here.
class question(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    question = models.CharField(max_length=500)
def __str__(self):
    return self.name

class answer(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    answer = models.CharField(max_length=500)
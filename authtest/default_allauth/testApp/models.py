#python manage.py makemigrations

from django.db import models

# Create your models here.

class SnsMessageModel(models.Model):
    user_id = models.IntegerField()
    message = models.CharField(max_length=100)

class SnsCommentModel(models.Model):
    snsmessagemodel_id = models.ForeignKey(SnsMessageModel,on_delete=models.CASCADE)
    message = models.CharField(max_length=100)

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MemoryModel(models.Model):
    title = models.CharField(max_length=100)
    for a in range (3):
        content_a = models.TextField()
    for i in range (5):
        images_i = models.ImageField(upload_to=None)
        images_comment_i = models.CharField(max_length=100)
        images_review_i = models.IntegerField(null=True,blank=True,default=0)
    
class PresentModel(models.Model):
    title = models.CharField(max_length=100)
    content_1 = models.TextField()
    content_2 = models.TextField()
    images = models.ImageField(upload_to=None)

class MemoryModel_1(models.Model):
    title = models.CharField(max_length=100)
    content_1 = models.TextField()
    content_2 = models.TextField(null=True, blank=True)
    content_3 = models.TextField(null=True, blank=True)
    images_1 = models.ImageField(upload_to=None)
    images_comment_1 = models.CharField(max_length=100,null=True, blank=True)
    images_review_1 = models.IntegerField(null=True,blank=True,default=0)
    images_2 = models.ImageField(upload_to=None,null=True, blank=True)
    images_comment_2 = models.CharField(max_length=100,null=True, blank=True)
    images_review_2 = models.IntegerField(null=True,blank=True,default=0)
    images_3 = models.ImageField(upload_to=None,null=True, blank=True)
    images_comment_3 = models.CharField(max_length=100,null=True, blank=True)
    images_review_3 = models.IntegerField(null=True,blank=True,default=0)
    images_4 = models.ImageField(upload_to=None,null=True, blank=True)
    images_comment_4 = models.CharField(max_length=100,null=True, blank=True)
    images_review_4 = models.IntegerField(null=True,blank=True,default=0)
    images_5 = models.ImageField(upload_to=None,null=True, blank=True)
    images_comment_5 = models.CharField(max_length=100,null=True, blank=True)
    images_review_5 = models.IntegerField(null=True,blank=True,default=0)

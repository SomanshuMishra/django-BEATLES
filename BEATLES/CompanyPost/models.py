from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from datetime import timezone
# Create your models here.
class PostsInfo(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=20)
    slug = models.SlugField(max_length = 130,unique=True)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.slug

class HandleSignUp(models.Model):

    username = models.CharField(max_length=255,unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=40)
    profile_pic = models.ImageField(null=True,blank=True)
    timeStamp_pass = models.DateTimeField(default=now) 

    def __str__(self):
        return 'User Name : ' +self.username


class PostComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField(blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(PostsInfo,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
    timestamp = models.DateTimeField(default=now)   

    def __str__(self):
        return f'{self.comment[0:5]}  on  {self.post}  '
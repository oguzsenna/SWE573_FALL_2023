from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db.models import Value



# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, null=False)
    username = models.CharField(unique =True, max_length=32)
    repassword = models.CharField(max_length=255)
    biography = models.TextField(blank=True)
    followers = models.ManyToManyField('self', related_name='following', symmetrical=False, blank=True)
    

class Story(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True)
    content = models.TextField(null=True)
    story_tags = ArrayField(models.CharField(max_length=255, null=True), default=list)
    location = models.CharField(max_length=255, null=True)
    date = models.DateField(null= True)
    likes = models.ManyToManyField(User, related_name='liked_stories', blank=True)


    def __str__(self):
        return self.title








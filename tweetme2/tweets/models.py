
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField, TextField
from rest_framework.serializers import ModelSerializer
from utils.models import AppBaseModel
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here
User = get_user_model()
# tweet composed by content , image, date and hour 
class TweetManager(models.Manager):
    def tweet_count(self):
        print("hellow word")

class TweetLike(models.Model):
    profile = models.ForeignKey("account.Profile",on_delete= CASCADE)  
    tweet = models.ForeignKey("Tweet",on_delete=models.CASCADE)  
    pub = models.DateField(auto_now_add=True)

class Retweet(models.Model):
    profile = models.ForeignKey("account.Profile",on_delete= CASCADE,related_name ='rprofile')  
    tweet = models.ForeignKey("Tweet",on_delete=models.CASCADE,related_name ='rtweet' )  
    pub = models.DateField(auto_now_add=True)

class Tweet (AppBaseModel):
    objects = TweetManager()
    user = models.ForeignKey(User,on_delete=models.CASCADE )
    content = models.TextField(blank = False, null =False)
    image = models.FileField(upload_to='images/',blank= True , null = True)
    likes = models.ManyToManyField("account.Profile",related_name='like',blank= True)
    retweets = models.ManyToManyField("account.Profile",related_name='retweet',blank= True)
    
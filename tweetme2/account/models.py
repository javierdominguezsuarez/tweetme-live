
from django.db import models

from django.contrib.auth import get_user_model
# Create your models here.
User =  get_user_model()
class FollowerRelation (models.Model):
    profile = models.ForeignKey("account.Profile",on_delete=models.CASCADE)
    pub = models.DateField(auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE)
    pub = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=220,null= True,blank = True)
    bio = models.TextField(blank = True , null = True)
    image = models.FileField(upload_to='images/',blank= True , null = True)
    followers = models.ManyToManyField('account.Profile',blank = True, related_name='following')

    """
    Querys
    project_obj = Profiles.objects.first()
    project_obj.followers.all()-> All porfiles following this profile
    user.following.all()-> All profiles i follow
    """

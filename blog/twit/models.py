from django.db import models 
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
   title = models.CharField(max_length=100,null=False)
   content = models.TextField()
   user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
   add_date = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   likes = models.BigIntegerField(default=0)
   is_public = models.BooleanField(default=True)
   views =models.BigIntegerField(default=0)
   




class UserProfile(models.Model):
   user=models.OneToOneField(User,on_delete=models.CASCADE)   


   

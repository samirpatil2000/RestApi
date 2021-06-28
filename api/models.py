from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


user=get_user_model()

class Text(models.Model):
    num=models.IntegerField(default=0,blank=True,null=True)
    name=models.CharField(default="Samir",blank=True,null=True,max_length=100)
    owner=models.ForeignKey(user,on_delete=models.SET_NULL,blank=True,null=True)
    def __str__(self):
        return self.name+str(self.pk)


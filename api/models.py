from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from django.utils.text import slugify
import random
user=get_user_model()

class Text(models.Model):

    num=models.IntegerField(default=0,blank=True,null=True)
    name=models.CharField(default="Samir"+str(random.randint(11,99)),blank=True,null=True,max_length=100)
    owner=models.ForeignKey(user,on_delete=models.SET_NULL,blank=True,null=True)
    slug=models.SlugField(max_length=100,blank=True,unique=True)
    self_refer=models.ForeignKey('self',blank=True,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name+str(self.pk)

    def save(self,*arg,**kwargs):
        if self.slug is None or self.slug=="" or self.slug==" ":
            self.slug=slugify(self.name+str(random.randint(11,99)))
            super(Text,self).save(*arg,**kwargs)





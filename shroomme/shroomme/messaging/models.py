from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class messages(models.Model):
	user1 = models.ForeignKey(settings.AUTH_USER_MODEL,blank = False,null = False)
	user2 = models.ForeignKey(settings.AUTH_USER_MODEL,blank = False,null = False,related_name="friends+")
	message = models.CharField(max_length=50,blank=False,null=False,default = "Unspecified")
	read = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	
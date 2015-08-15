from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from constants.constants import constants
import uuid
# Create your models here.




class Profile(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.OneToOneField(settings.AUTH_USER_MODEL,blank = False,null = False)
	first_name = models.CharField(max_length=50,blank=False,null=False,default = "Unspecified")
	middle_name = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
	last_name = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
	nationality = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
	university = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
	gender = models.CharField(max_length=1,choices=constants.GENDER_CHOICES,default='U')
#	middle_name = models.TextField(null=True,blank=True)
#	last_name =  models.TextField(null=True,blank=True)
#	nationality = models.TextField(null=True,blank=True)

class Friends(models.Model):
	user1 = models.ForeignKey(settings.AUTH_USER_MODEL,blank = False,null = False)
	user2 = models.ForeignKey(settings.AUTH_USER_MODEL,blank = False,null = False,related_name="friends+")
	#timestamp
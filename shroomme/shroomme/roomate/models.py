from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.conf import settings
from constants.constants import constants
import uuid,os
from django.db.models import Q
#from userprofile.models import Profile
#from 
# Create your models here.

class RoomateManager(models.Manager):
	#--USED TO ROOMATE OBJECT FROM user1 = from user2 = to
	def get_object_from(self,user1_uuid,user2_uuid):
		c1 = Q(user1_uuid=user1_uuid)
		c2 = Q(user2_uuid=user2_uuid)
		c3 = Q(user1_uuid=user2_uuid)
		c4 = Q(user2_uuid=user1_uuid)

		temp = self.filter((c1&c2)|(c3&c4))
		if len(temp) == 0:
			return None
		elif temp is None:
			return None
		else:
			return temp[0]




class Criteria(models.Model):
	user_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
	#---CHAR FIELD-----_#
	major = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
	hobby = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
	#-----CHOICES---------#
	smoke = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
	pet = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
	relationship_status = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
	gender = models.CharField(max_length=1,choices=constants.GENDER_CHOICES,default='U')
	nationality = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
	#------SCALE----------#
	cleanliness = models.IntegerField(choices= constants.LEVEL,default = 0)	
	sleeping_habit = models.IntegerField(choices= constants.LEVEL,default = 0)
	drinking = models.IntegerField(choices= constants.LEVEL,default = 0)
	noisiness = models.IntegerField(choices= constants.LEVEL,default = 0)
	overnight_guests = models.IntegerField(choices= constants.LEVEL,default = 0)
	cooking = models.IntegerField(choices= constants.LEVEL,default = 0)
	budget = models.IntegerField(default = 0)


class Roomate(models.Model):
	user1 = models.ForeignKey(settings.AUTH_USER_MODEL,blank = True,null = True)
	user2 = models.ForeignKey(settings.AUTH_USER_MODEL,blank = True,null = True,related_name="roomate+")
	user1_uuid = models.UUIDField(default=uuid.uuid4,blank = True,null = True)
	user2_uuid = models.UUIDField(default=uuid.uuid4,blank = True,null = True)
	status = models.CharField(max_length=1,choices=constants.ROOMATE_STATUS_II,default='U')
	created = models.DateTimeField(auto_now_add=True,blank = True,null = True)
	roomate_id = models.UUIDField(primary_key = True, default=uuid.uuid4)#, editable=False)
#	id = models.IntegerField(primary_key = True,default = 0)
	objects = models.Manager()
	manager = RoomateManager()




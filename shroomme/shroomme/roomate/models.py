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
	def getMyRoomates(self,uuid):
		return self.all()	
	def getRoomatesFor(self,uuid):
		return self.all()	
	def makePendingStatus(self,user1,user2):
		return self.all()	
	def getStatus(self,user1,user2):
		c1 = Q(user1=user1)
		c2 = Q(user2=user2)
		c3 = Q(user1=user2)
		c4 = Q(user2=user1)
		roomate_object = self.filter( ( (c1&c2)|(c3&c4)) )
		if not roomate_object:
			return "N"
		status = roomate_object[0].status
		return status
	def getRoomates(self,user1):
		from userprofile.models import Profile		
		c1 = Q(user1= user1)
		c2 = Q(user2= user1)
		c3 = Q(status='R')
		roomate_list = self.filter( (c1|c2) & c3 )
		uuid1 = roomate_list.values_list('user1_uuid','status')
		print uuid1
		uuid2 = roomate_list.values_list('user2_uuid','status')
		uuid1zip = zip(*uuid1)[0]
		uuid2zip = zip(*uuid2)[0]
		uuidtotal = list(set(uuid1zip + uuid2zip))
		result_list = []
		if uuid_total is None:
			result_list = []
		else:
			uuid_total.remove(uuid1)
			result_list = Profile.objects.filter(id__in=uuid_total)
		return result_list



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
	roomate_id = models.UUIDField(primary_key=True, default=uuid.uuid4)#, editable=False)
	manager = RoomateManager()




from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from constants.constants import constants
import uuid,os



#----------------user1 = user from---------------------#
#----------------user2 = user to-----------------------#

class NotificationManager(models.Manager):

	def createFriendNotification(self):
		print "createFriend";

	def createRoomateNotification(self):
		print "createRoomate";



# Create your models here.
class Notification(models.Model):
	user1 = models.ForeignKey(settings.AUTH_USER_MODEL,blank = False,null = False)
	user2 = models.ForeignKey(settings.AUTH_USER_MODEL,null = False,related_name="notification+")
	user1_uuid = models.UUIDField(blank = True,null = True)
	user2_uuid = models.UUIDField(blank = True,null = True)
	message = models.CharField(max_length=50,blank=False,null=False,default = "Unspecified")
	read = models.BooleanField(default = False)
	created = models.DateTimeField(auto_now_add=True)
	notification_type = models.CharField(max_length=2,choices=constants.NOTIFICATION_TYPE,default="FR")
	notification_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	target_id = models.UUIDField(default=uuid.uuid4,blank = False) #--> conversation ID + friend_relation ID 
	
#	friends_id = models.UUIDField(default=uuid.uuid4)
#	conversation = models.UUIDField(default=uuid.uuid4)





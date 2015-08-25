from django.db import models
from constants.constants import constants
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Q
import uuid

# Create your models here.
class Friends(models.Model):
	user1 = models.ForeignKey(settings.AUTH_USER_MODEL,blank = False,null = False)
	user2 = models.ForeignKey(settings.AUTH_USER_MODEL,blank = False,null = False,related_name="friends+")
	user1_uuid = models.UUIDField(blank = True,null = True)
	user2_uuid = models.UUIDField(blank = True,null = True)
	status = models.CharField(max_length=1,choices=constants.FRIEND_STATUS,default='U')
	created = models.DateTimeField(auto_now_add=True)
	friends_id = models.UUIDField(primary_key=True, default=uuid.uuid4)#, editable=False)


def isFriends(user1,user2):
	c1 = Q(user1=user1)
	c2 = Q(user2=user2)
	c3 = Q(user1=user2)
	c4 = Q(user2=user1)
	friend_object = Friends.objects.filter( ( (c1&c2)|(c3&c4)) )
#	friend_object = Friends.objects.filter( ( c1&c2 ) )
	if friend_object is None:
		return False
	status = friend_object[0].status
	if status == "F":
		return True
	else:
		return False

def getStatus(user1,user2):
	c1 = Q(user1=user1)
	c2 = Q(user2=user2)
	c3 = Q(user1=user2)
	c4 = Q(user2=user1)
	friend_object = Friends.objects.filter( ( (c1&c2)|(c3&c4)) )
	if not friend_object:
		return "N"
	status = friend_object[0].status
	return status


def getFriendsObject(user1,user2):
	c1 = Q(user1=user1)
	c2 = Q(user2=user2)
	c3 = Q(user1=user2)
	c4 = Q(user2=user1)
	friend_object = Friends.objects.get( ( (c1&c2)|(c3&c4)) )
	return friend_object
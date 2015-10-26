from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models import Q
import uuid

# Create your models here.
class messages(models.Model):
	user1 = models.ForeignKey(settings.AUTH_USER_MODEL,blank = True,null = True)
	user2 = models.ForeignKey(settings.AUTH_USER_MODEL,blank = True,null = True,related_name="friends+")
	user1_uuid = models.UUIDField(blank = True,null = True)
	user2_uuid = models.UUIDField(blank = True,null = True)
	message = models.CharField(max_length=50,blank=False,null=False,default = "Unspecified")
	read = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True)
	



class rooms(models.Model):
	user_uuid = models.UUIDField(blank = True) #change into array
	room_uuid = models.UUIDField(blank = True,default=uuid.uuid4)
	timestamp = models.DateTimeField(auto_now_add=True)

class message_room(models.Model):
	room_uuid = models.UUIDField(blank = True,default=uuid.uuid4)
	user_uuid = models.UUIDField(blank=True,null = True)
	message = models.CharField(max_length=50,blank=False,null=False,default = "Unspecified")
	timestamp = models.DateTimeField(auto_now_add=True)


def getMessages(user1_uuid,user2_uuid):
	c1 = Q(user1_uuid=user1_uuid)
	c2 = Q(user2_uuid=user2_uuid)
	c3 = Q(user1_uuid=user2_uuid)
	c4 = Q(user2_uuid=user1_uuid)
	message_list = messages.objects.filter((c1&c2)|(c3&c4)).order_by('timestamp')
	return message_list

def getUpdates(user1_uuid,user2_uuid,counter):
	temp = getMessages(user1_uuid,user2_uuid)
	target_size = len(temp) - counter
	message_list = []

	for a in range(0,target_size):
		message_list.append(temp[a+counter])
	return message_list



def getRooms(user_uuid):
	return rooms.objects.filter(user_uuid = user_uuid)

def getRoomMessages(room_uuid):
	return message_room.filter(room_uuid = room_uuid).order_by('-timestamp')



#--------------------EXPERIMENTAL---------------------------#

class threads(models.Model):
	user_uuid = models.UUIDField(blank = True) #change into array
	thread_id = models.UUIDField(blank = True)

class thread_messages(models.Model):
	thread_id = models.UUIDField(blank = True)
	user_uuid = models.UUIDField(blank=True,null = True)
	message = models.CharField(max_length=50,blank=False,null=False,default = "Unspecified")
	timestamp = models.DateTimeField(auto_now_add=True)


from django.db import models
from constants.constants import constants
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Q
from userprofile.models import Profile
import uuid

# Create your models here.


class friends_manager(models.Manager):
	#--USED TO FRIENDS OBJECT FROM user1 = from user2 = to
	def get_object_from(self,user1_uuid,user2_uuid):
		c1 = Q(user1_uuid=user1_uuid)
		c2 = Q(user2_uuid=user2_uuid)
		temp = self.filter((c1&c2))
		if len(temp) == 0:
			return None
		elif temp is None:
			return None
		else:
			return temp[0]




class Friends(models.Model):
	user1 = models.ForeignKey(settings.AUTH_USER_MODEL,blank = False,null = False)
	user2 = models.ForeignKey(settings.AUTH_USER_MODEL,blank = False,null = False,related_name="friends+")
	user1_uuid = models.UUIDField(blank = True,null = True)
	user2_uuid = models.UUIDField(blank = True,null = True)
	status = models.CharField(max_length=1,choices=constants.FRIEND_STATUS,default='U')
	created = models.DateTimeField(auto_now_add=True)
	friends_id = models.UUIDField(primary_key=True, default=uuid.uuid4)#, editable=False)
	user1_messages_count = models.IntegerField(default = 0)
	user2_messages_count = models.IntegerField(default = 0)
	user1_last_received = models.DateTimeField(blank = True,auto_now_add=True)
	user2_last_received =  models.DateTimeField(blank = True,auto_now_add=True)
	manager = friends_manager()

	def test(self):
		return self.objects.all()


def isFriends(user1,user2):
	c1 = Q(user1=user1)
	c2 = Q(user2=user2)
	c3 = Q(user1=user2)
	c4 = Q(user2=user1)
	friend_object = Friends.objects.filter( ( (c1&c2)|(c3&c4)) )
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
	friend_object = Friends.objects.filter( ( (c1&c2)|(c3&c4)) )
	return friend_object[0]


def getMyFriendsMessaging(request):
	c1 = Q(user1=request.user)
	c2 = Q(user2=request.user)
	c3 = Q(status='F')
	friends_list = Friends.objects.filter( (c1|c2) & c3 )
	uuid_1 = friends_list.values_list('user1_uuid','status')
	uuid_2 = friends_list.values_list('user2_uuid','status')
	uuid_1zip = zip(*uuid_1)[0]
	uuid_2zip = zip(*uuid_2)[0]
	uuid_total = list(set(uuid_1zip + uuid_2zip))
	result_list = []
	if uuid_total is None:
		result_list = []
	else:
		uuid_total.remove(Profile.objects.get(user=request.user).id)
		result_list = Profile.objects.filter(id__in=uuid_total)
	return result_list

def getMyFriends(request):
	c1 = Q(user1=request.user)
	c2 = Q(user2=request.user)
	c3 = Q(status='F')
	friends_list = Friends.objects.filter( (c1|c2) & c3 )
	uuid_1 = friends_list.values_list('user1_uuid','status')
	uuid_2 = friends_list.values_list('user2_uuid','status')
	uuid_1zip = zip(*uuid_1)[0]
	uuid_2zip = zip(*uuid_2)[0]
	uuid_total = list(set(uuid_1zip + uuid_2zip))
	result_list = []
	if uuid_total is None:
		result_list = []
	else:
		uuid_total.remove(Profile.objects.get(user=request.user).id)
		result_list = Profile.objects.filter(id__in=uuid_total)
	return result_list




#---------------- 2 WAY BOUNDING ------------------------------- #
# def isFriends(user1,user2):
# 	c1 = Q(user1=user1)
# 	c2 = Q(user2=user2)
# 	c3 = Q(user1=user2)
# 	c4 = Q(user2=user1)
# 	friend_object = Friends.objects.filter( ( (c1&c2)|(c3&c4)) )
# #	friend_object = Friends.objects.filter( ( c1&c2 ) )
# 	if friend_object is None:
# 		return False
# 	status = friend_object[0].status
# 	if status == "F":
# 		return True
# 	else:
# 		return False

# def getStatus(user1,user2):
# 	c1 = Q(user1=user1)
# 	c2 = Q(user2=user2)
# 	c3 = Q(user1=user2)
# 	c4 = Q(user2=user1)
# 	friend_object = Friends.objects.filter( ( (c1&c2)|(c3&c4)) )
# 	if not friend_object:
# 		return "N"
# 	status = friend_object[0].status
# 	return status


# def getFriendsObject(user1,user2):
# 	c1 = Q(user1=user1)
# 	c2 = Q(user2=user2)
# 	c3 = Q(user1=user2)
# 	c4 = Q(user2=user1)
# 	friend_object = Friends.objects.get( ( (c1&c2)|(c3&c4)) )
# 	return friend_object

# def getMyFriends(request):
# 	c1 = Q(user1=request.user)
# 	c2 = Q(user2=request.user)
# 	c3 = Q(status='F')
# 	friends_list = Friends.objects.filter( (c1|c2) & c3 )
# 	uuid_1 = friends_list.values_list('user1_uuid','status')
# 	uuid_2 = friends_list.values_list('user2_uuid','status')
# 	uuid_1zip = zip(*uuid_1)[0]
# 	uuid_2zip = zip(*uuid_2)[0]
# 	uuid_total = list(set(uuid_1zip + uuid_2zip))
# 	result_list = []
# 	if uuid_total is None:
# 		result_list = []
# 	else:
# 		uuid_total.remove(Profile.objects.get(user=request.user).id)
# 		result_list = Profile.objects.filter(id__in=uuid_total)
# 	return result_list



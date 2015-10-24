from constants.constants import constants,gethome
from django.shortcuts import render,redirect
from django.views.decorators.csrf import requires_csrf_token

#-----------MODELS IMPORT-----------------------------------#
from .models import Friends
from django.contrib.auth.models import User
from userprofile.models import Profile
from notification.models import Notification
from django.db.models import Q
import uuid



def show_friends(request):
	c1 = Q(user1=request.user)
	c2 = Q(user2=request.user)
	c3 = Q(status='F')
	friends_list = Friends.objects.filter( (c1|c2) & c3 )
	uuid_1 = friends_list.values_list('user1_uuid','status')
	uuid_2 = friends_list.values_list('user2_uuid','status')
	uuid_1zip = zip(*uuid_1)[0]
	uuid_2zip = zip(*uuid_2)[0]
	uuid_total = list(set(uuid_1zip + uuid_2zip))
	if uuid_total is None:
		context = {}		
	else:
		print uuid_total		
		print Profile.objects.get(user=request.user).id
		uuid_total.remove(Profile.objects.get(user=request.user).id)
		print "TITIT---------------------------------"
		result_list = Profile.objects.filter(id__in=uuid_total)
		context = {"result_list":result_list}
	return render(request,"show_friends.html",context)

@requires_csrf_token
def add_friend(request):
	if not request.user.is_authenticated():
		return redirect(gethome())
	if request.method != 'POST':
		return redirect(gethome())
	else:			
		print "HELLO I AM AT AN AJAX CALL AT FRIENDS.VIEW.add_friend-----------------------------------------------------"
		print request.POST
		if "user2" in request.POST:
			user2_id = request.POST["user2"] 
			Profile2_object = Profile.objects.filter(id=user2_id)
			user2 = Profile2_object[0].user
			user1 = request.user #user who clicked add friend ==> userFrom

			message = Profile2_object[0].first_name + " " + Profile2_object[0].last_name + " wants to be friends with you"
			if checkFriendExisted(user1,user2) == True:
				return redirect(gethome())
			#-------------BETA-------------------------------------#
			user2_uuid = Profile2_object[0].id
			user1_uuid = Profile.objects.filter(user=user1)[0].id
			#-------------BETA-------------------------------------#
			friend_object = Friends(user1=user1,user2=user2,status = "P",user1_uuid=user1_uuid,user2_uuid=user2_uuid)
			friend_object.save()
			if(checkNotificationExisted(user1,user2,"F") == False):
				notification_object = Notification( user1=user1,
													user2=user2,
													message=message,
													read=False,
													notification_type="FR",
													target_id=friend_object.friends_id,
													user1_uuid=user1_uuid,
													user2_uuid=user2_uuid)
				notification_object.save()
			print "-------------DONE-----------------"
		return redirect(gethome())


@requires_csrf_token
def change_friend_status(request):
	if not request.user.is_authenticated():
		return redirect(gethome())

	if request.method != 'POST':
		print "NOT POST-----------------"
		return redirect(gethome())
	else:
		print "CHANGE REQUEST ENTER AJAX CALL--------------------------"
		print request.POST
		notification_id = request.POST['this_id']
		notification_object = Notification.objects.filter(notification_id=notification_id)
		response_type = str(request.POST['type']) 
		if "delete_notification" == response_type:
			print "DELETe NOTIFICATION--------------------AJAX------------------"			
			notification_object.delete()
			return redirect(gethome())

		target_id = request.POST['target_id']
		friend_object = Friends.objects.filter(friends_id=target_id)				
		#-------------BETA-------------------------------------#			
		user1_uuid = request.POST['user1_uuid']
		user2_uuid = request.POST['user2_uuid']
		#-------------BETA-------------------------------------#	
		if "accept" == response_type:
			print "ACCEPT-------------------AJAX------------------"
			friend_object.update(status="F")			
			notification_object.delete()
			#-------------BETA-------------------------------------#			
			profile1 = Profile.objects.get(id=user1_uuid)
			profile2 = Profile.objects.get(id=user2_uuid)
			#-------------BETA-------------------------------------#
			message =  str(profile2.first_name) + " " +str(profile2.last_name) +" " +"HAVE BECOME FRIENDS WITH YOU"
			accept_notification = Notification( user1=profile2.user,
												user2=profile1.user,
												message=message,
												user1_uuid=user2_uuid,
												user2_uuid=user1_uuid,
												notification_type="FA")
			accept_notification.save()
		elif "ignore" == response_type:
			print "IGNORE-------------------AJAX------------------"
			friend_object.delete()						
			notification_object.delete()			
		elif "block" == response_type:
			print "BLOCK--------------------AJAX------------------"
	return redirect(gethome())


def checkFriendExisted(user1,user2):
	c1 = Q(user1=user1)
	c2 = Q(user2=user2)
	c3 = Q(user1=user2)
	c4 = Q(user2=user1)
	friend_object = Friends.objects.filter((c1 & c2)|(c3 & c4))
	if not friend_object:
		return False

	if friend_object[0].status == 'P' or friend_object[0].status == 'F':
		return True
	else:
		return False



def checkNotificationExisted(user1,user2,notification_type):
	criterion1 = Q(user1=user1)
	criterion2 = Q(user2=user2)
	criterion3 = Q(notification_type=notification_type)
	notification_object = Notification.objects.filter(criterion1 & criterion2 & criterion3)
	if not notification_object:
		return False
	else:
		return True




from django.shortcuts import render
from friends.models import Friends,getMyFriends,getMyFriendsMessaging
from django.http import HttpResponse,JsonResponse
from userprofile.models import Profile
from .models import messages,getMessages,getRooms,getRoomMessages,getUpdates,threads,thread_messages
from django.db.models import Q


import json
from json import JSONEncoder
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
import uuid

def show_messaging(request):
	my_friends = getMyFriendsMessaging(request)
	my_uuid = Profile.objects.get(user=request.user).id
	import pdb; pdb.set_trace()
	testz = Friends.test()
	context = {"my_friends":my_friends,"my_uuid":my_uuid}
	return render(request,"show_messaging.html",context)


def show_messaging_2(request):
	my_uuid = Profile.objects.get(user=request.user).id
	thread_list = threads.objects.filter(user_uuid=my_uuid)
	name_list = []
	for elem in thread_list:
		user_list = threads.objects.filter(thread_id = elem.thread_id)
		temp_names = []
		for elem_2 in user_list:
			if my_uuid == elem_2.user_uuid:
				continue
			profile_object = Profile.objects.get(id=elem_2.user_uuid)
			name = profile_object.first_name + " " + profile_object.last_name
			temp_names.append(name)
		name_list.append(temp_names)


	context = {"thread_list":thread_list,"my_uuid":my_uuid,"name_list":name_list}
	return render(request,"show_messaging_2.html",context)

def create_message_2(request):
	user_list = Profile.objects.all()
	my_uuid = Profile.objects.get(user=request.user).id
	context = {"user_list":user_list,"my_uuid":my_uuid}
	return render(request,"create_message_2.html",context)




#---------------------------------AJAX MESSAGES-------------------------------#
def show_messages(request):
	print "AJAX CALL MESSAGES.SHOW_MESSAGES"
	if request.method == "POST" and request.is_ajax():
		user1_uuid = request.POST['user1_uuid']
		user2_uuid = request.POST['user2_uuid']
		message_list = getMessages(user1_uuid,user2_uuid)#.values_list()
#		message_json = json.dumps(list(message_list), cls=DjangoJSONEncoder)
		user1_object = Profile.objects.get(id=user1_uuid)
		user2_object = Profile.objects.get(id=user2_uuid)
		user1_name = user1_object.first_name + " " + user1_object.last_name
		user2_name = user2_object.first_name + " " + user2_object.last_name
	
		message_list=serializers.serialize("json", message_list) 
		context = {"message_list":message_list,"user1_name":user1_name,"user2_name":user2_name}
		return JsonResponse(context)
	else:
		context = {"name":"failure"}
		return HttpResponse(json.dumps(context), content_type="application/json");

def create_messages(request):
	if request.method == "POST" and request.is_ajax():
		user1_uuid = request.POST['user1_uuid']
		user2_uuid = request.POST['user2_uuid']		
		message = request.POST['message']
		messageCounter = int(request.POST['messageCounter'])
		message_object = messages(user1_uuid=user1_uuid,
								  user2_uuid=user2_uuid,
								  message =message)
		message_object.save()
		message_list = getUpdates(user1_uuid,user2_uuid,messageCounter)
		message_list = serializers.serialize("json", message_list) 
		context = {"message_list":message_list}
		return JsonResponse(context)
	else:
		return render(request,"index.html",{})

def update_messages(request):
	if request.method == "POST" and request.is_ajax():
		user1_uuid = request.POST['user1_uuid']
		user2_uuid = request.POST['user2_uuid']		
		messageCounter = int(request.POST['messageCounter'])
		message_list = getUpdates(user1_uuid,user2_uuid,messageCounter)
		message_list = serializers.serialize("json", message_list) 
		context = {"message_list":message_list}
		return JsonResponse(context)
	else:
		return render(request,"index.html",{})

def create_thread(request):
	if request.method == "POST" and request.is_ajax():
		print request.POST
		user_list = request.POST['user_list']
		user_list = json.loads(user_list)
		print "USER_LIST------------------"
		print user_list
		message = request.POST['message']
		my_uuid = Profile.objects.get(user=request.user).id
		thread_id = uuid.uuid1()
		thread_object= threads(
					user_uuid = my_uuid,
					thread_id = thread_id
			)
		thread_object.save()

		for elem in user_list:
			print "ELEM------------"
			print elem
			thread_object= threads(
					user_uuid = elem,
					thread_id = thread_id						
				)
			thread_object.save()
		thread_messages_object = thread_messages(
				user_uuid = my_uuid,
				thread_id = thread_id,
				message	= message				
			)
		thread_messages_object.save()
		return render(request,"index.html",{})
	else:
		return render(request,"index.html",{})

def get_thread_list(request):
	return 0;

def get_thread_messages(request):
	return 0;



def group_message(request):
	return "asdf"


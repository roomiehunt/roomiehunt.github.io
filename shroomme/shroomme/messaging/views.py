from django.shortcuts import render
from friends.models import Friends,getMyFriends
from django.http import HttpResponse,JsonResponse
from userprofile.models import Profile
from .models import messages,getMessages,getRooms,getRoomMessages,getUpdates
from django.db.models import Q


import json
from json import JSONEncoder
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from uuid import UUID


# Create your views here.
def show_messaging(request):
	my_friends = getMyFriends(request)
	my_uuid = Profile.objects.get(user=request.user).id
	context = {"my_friends":my_friends,"my_uuid":my_uuid}
	return render(request,"show_messaging.html",context)

#---------------------------------AJAX GET MESSAGES-------------------------------#
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






def group_message(request):
	return "asdf"


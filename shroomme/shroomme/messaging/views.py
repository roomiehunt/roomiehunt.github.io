from django.shortcuts import render
from friends.models import Friends,getMyFriends
from django.http import HttpResponse,JsonResponse
from userprofile.models import Profile
from .models import messages,getMessages,getRooms,getRoomMessages
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
		message_list = getMessages(user1_uuid,user2_uuid).values_list()
		message_json = json.dumps(list(message_list), cls=DjangoJSONEncoder)

#		message_list=serializers.serialize("json", message_list) 
		context = {"message_list":message_list}
		return JsonResponse(context)
	else:
		context = {"name":"failure"}
		return HttpResponse(json.dumps(context), content_type="application/json");

def create_message(request):
	if request.method == "POST" and request.is_ajax():
		user1_uuid = request.POST['user1_uuid']
		user2_uuid = request.POST['user2_uuid']		
		message = request.POST['message']
		#Create message object
		message_object = messages(user1_uuid=user1_uuid,
								  user2_uuid=user2_uuid,
								  message =message)
		#Save it to database
		message_object.save()
		return render(request,"index.html",{})
	else:
		return render(request,"index.html",{})

def group_message(request):
	return "asdf"


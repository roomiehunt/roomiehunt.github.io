from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Notification
from friends.models import Friends
from django.db.models import Q
from messaging.models import messages


# Create your views here.
def show_notification(request):
	notification_result = Notification.objects.filter(user2=request.user)
	#------------------------------#
	#	example_object = notification_result[0]
	#	username = example_object.user1
	#	print "USERNAME " + str(username)
	#	print notification_result.values()[0]
	#	print notification_result.values()[0][u'user1_id']
	#------------------------------#
	context = {"notification_result":notification_result}
	return render(request,"show_notification.html",context)


def notification_count(request):
	return render(request,"index.html",{})
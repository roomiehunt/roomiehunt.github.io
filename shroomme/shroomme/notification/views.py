from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Notification
from friends.models import Friends
from django.db.models import Q
from messaging.models import messages


# Create your views here.
def show_notification(request):
	#----> user1 = From , user2 = To
	notification_result = Notification.objects.filter(user2=request.user)
	context = {"notification_result":notification_result}
	return render(request,"show_notification.html",context)

def notification_count(request):
	return render(request,"index.html",{})

#--------------ajax-------------------
def delete_notification(request):
	if request.is_ajax() and request.method == "POST":
		notification_id = request.POST["notification_id"]
		notification_object	= Notification.objects.get(notification_id=notification_id)
		notification_object.delete()
		return render(request,"index.html",{})
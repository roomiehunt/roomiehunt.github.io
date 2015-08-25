from django.shortcuts import render,Http404,redirect,render_to_response
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import ProfileForm,SearchForm,EditForm
from shroomme.forms import LoginForm,SignUpForm

#-----------------------------------MODELS-------------------------#
from django.contrib.auth.models import User
from .models import Profile
from django.db.models import Q
from django.forms.models import model_to_dict
from friends.models import Friends,getStatus,getFriendsObject
from constants.constants import constants,gethome
from notification.models import Notification

#from shroomme.views import home
 
#@login_required('')
def myprofile(request):
	print "login-request:"
	print request
	if request.user.is_authenticated():
		myuser = request.user
		result = Profile.objects.filter(user = request.user).values() #SELECT ALL FROMM PROFILE WHERE USER = MYUSER
		context = {"result":result}
		return render(request,'myprofile.html',context)
	else:
#		from shroomme.views import home
		return redirect(gethome())

def edit_profile(request):
	if request.user.is_authenticated():
		my_profile = Profile.objects.filter(user=request.user).values()
		edit = EditForm()
		context = {"profile":my_profile[0],"edit":edit}
		return render(request,'edit_profile.html',context)
	else:
		return redirect(gethome())

def first_time_user(request):
	print "first_time_user:" 
	print request
	if request.user.is_authenticated():
		#if not first time redirect(myprofile)!!!
		if 'submit' in request.POST and request.method == 'POST':
			myForm = ProfileForm(request.POST)
			first_name = myForm.data['first_name']
			middle_name = myForm.data['middle_name']
			last_name = myForm.data['last_name']
			nationality =myForm.data['nationality']
			gender = myForm.data['gender']
			myProfile = Profile.objects.select_for_update().filter(user=request.user)
			myProfile.update(first_name=first_name,middle_name=middle_name,last_name=last_name)
			#myProfile.update()
			if myForm.is_valid():
				print "FIRST_TIME_USER FORM VALID POSTED"
				print request.POST
			else:
				print "FIRST_TIME_USER FORM INVALID POSTED"	
				print request.POST
			return redirect(gethome())
		else:
			myForm = ProfileForm()
			context = {"form":myForm}
			return render(request,'first_time_user.html',context)
	else:
		return render(request,'error_login.html',{})

def logout_view(request):
	logout(request)
	return redirect(gethome())

def find_people(request):
	result = ()
	login = LoginForm()
	signup = SignUpForm()
	if request.user.is_authenticated():
		if request.method == 'GET':
			print request.GET
			if 'university' in request.GET:
				searchbar = SearchForm(request.GET)
				print "I am searching for " + str(request.GET['university'])
				query_text = request.GET['university']
				#------------TRY CRITERIONS FOR ANDS------------------# Q model object django
				nationality = ""
				criterion1 = Q(university=query_text)
				criterion2 = Q(nationality=nationality)
				result = Profile.objects.filter(university = query_text)
				result = result.exclude(user=request.user)
				context = {'searchbar':searchbar,"result":result,"request":request}
				return render(request,'find_people.html',context)
			else:		#--------------------IF SEARCH BAR IS FILLED RANDOMLY-----#
				searchbar = SearchForm()
				context = {'searchbar':searchbar,"result":result,"request":request}
				return render(request,'find_people.html',context)
		else:	#-----------------------IF METHOD IS NOT GET----------------------#
			searchbar = SearchForm()
			context = {'searchbar':searchbar,"result":result,"request":request}
			return render(request,'find_people.html',context)
	else:
#		return redirect(gethome())
		searchbar = SearchForm()
		context = {'searchbar':searchbar,"result":result,"request":request,"login":login,"signup":signup}
		return render(request,'find_people.html',context)


def show_user(request):
	if request.user.is_authenticated():
		if request.method == 'GET':
			profile_id = request.GET['profile_id']
			print "profile_id " + profile_id
			profile = Profile.objects.filter(id=profile_id)
			friends_status = getStatus(request.user,profile[0].user)
			friends_object = getFriendsObject(request.user,profile[0].user)
			context = {"profile":profile[0],"friend_status":friends_status}
			if friends_status == 'P':
				friends_id = friends_object.friends_id
				notification_object = Notification.objects.get(target_id=friends_id)
				user1_uuid = notification_object.user1_uuid
				user2_uuid = notification_object.user2_uuid
				this_id = notification_object.notification_id
				additional_context = {"target_id":friends_id,
									  "user1_uuid":user1_uuid,
									  "user2_uuid":user2_uuid,
									  "this_id":this_id}
				context.update(additional_context)
			print "CONTEXT-------------------"
			print "CONTEXT-------------------"
			print context
			return render(request,'show_user.html',context)
	return redirect(gethome())




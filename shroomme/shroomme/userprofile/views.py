from django.shortcuts import render,Http404,redirect,render_to_response
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import ProfileForm,SearchForm,EditForm,UploadProfileImage
from shroomme.forms import LoginForm,SignUpForm

#-----------------------------------MODELS-------------------------#
from django.contrib.auth.models import User
from .models import Profile
from django.db.models import Q
from django.forms.models import model_to_dict
from friends.models import Friends,getStatus,getFriendsObject
from constants.constants import constants,gethome
from notification.models import Notification
from roomate.forms import CriteriaForm
import os

#from shroomme.views import home
 
#@login_required('')
def myprofile(request):
	print "login-request:"
	print request
	if request.user.is_authenticated():
		UploadForm = UploadProfileImage(request.POST or None)
		this_user = Profile.objects.get(user = request.user) 
		if request.method == 'POST':
			print request.POST
			print request.FILES
			if request.FILES:
				update_object = Profile.objects.select_for_update().filter(user=request.user)
				print "SUCCESS"
				file_name =  str(this_user.id) +".jpg"
				print file_name
				handle_uploaded_file(request.FILES['user_image'],file_name)
				location = '/static/photos/' + file_name
				update_object.update(profile_image = location)
		context = {"myprofile":this_user,"form":UploadForm}
		return render(request,'myprofile.html',context)
	else:
		return redirect(gethome())


def first_time_user(request):
	if request.user.is_authenticated():
		myForm = ProfileForm(request.POST or None)
		if request.method == "POST" and myForm.is_valid():
			first_name = myForm.data['first_name']
			middle_name = myForm.data['middle_name']
			last_name = myForm.data['last_name']
			nationality =myForm.data['nationality']
			gender = myForm.data['gender']
			myProfile = Profile.objects.select_for_update().filter(user=request.user)
			myProfile.update(first_name=first_name,middle_name=middle_name,last_name=last_name)
			return redirect(gethome())
		else:
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
		searchbar = SearchForm()
		context = {'searchbar':searchbar,"result":result,"request":request,"login":login,"signup":signup}
		return render(request,'find_people.html',context)


#This function is used to show the information of another user
def show_user(request):
	if request.user.is_authenticated():
		if request.method == 'GET':
			profile_id = request.GET['profile_id']
			target_profile = Profile.objects.get(id=profile_id) #---> GET TARGET PROFILE
			context = {"profile":target_profile,"interest":"none"}			
#			friends_status = getStatus(request.user,profile.user) #--OLD CODE
			my_user = request.user
			my_profile = Profile.objects.get(user=my_user)
			user1_uuid = my_profile.id
			user2_uuid = target_profile.id 
			friends_object12 = Friends.manager.get_object_from(user1_uuid,user2_uuid)
			friends_object21 = Friends.manager.get_object_from(user2_uuid,user1_uuid)
			if friends_object12 is not None:
				if friends_object21 is not None:
					if friends_object12.status == "I" and friends_object21.status =="I":
						context.update( {"interest":"mutual"} )
				else:
					if friends_object12.status == "I":
						context.update({"interest":"pending"})
			else:
				if friends_object21 is not None:
					if friends_object21.status == "I":
						context.update({"interest":"interested"})
			# if friends_status == 'P':
			# 	friends_object = getFriendsObject(request.user,profile.user)				
			# 	friends_id = friends_object.friends_id
			# 	notification_object = Notification.objects.get(target_id=friends_id)
			# 	user1_uuid = notification_object.user1_uuid
			# 	user2_uuid = notification_object.user2_uuid
			# 	my_uuid = Profile.objects.get(user=request.user).id
			# 	this_id = notification_object.notification_id
			# 	additional_context = {"target_id":friends_id,
			# 						  "my_uuid":my_uuid,
			# 						  "user1_uuid":user1_uuid,
			# 						  "user2_uuid":user2_uuid,
			# 						  "this_id":this_id,
			# 						  "friends_object":friends_object
			# 						  }
			# 	context.update(additional_context)
			return render(request,'show_user.html',context)
	return redirect(gethome())


def edit_profile(request):
	if request.user.is_authenticated():
		my_profile = Profile.objects.filter(user=request.user)
		edit = EditForm(request.POST or None,request.FILES or None ,instance = my_profile[0])		
		if edit.is_valid():
			#print "EDIT PROFILE--------------------------------------------"
			instance = edit.save(commit=False)
			instance.save()
		context = {"profile":my_profile[0],"edit":edit}
		return render(request,'edit_profile.html',context)
	else:
		return redirect(gethome())

def my_criteria(request):
	my_profile = Profile.objects.get(user= request.user)
	form = CriteriaForm(request.POST or None,instance = my_profile.myCriteria)
	if form.is_valid():
		myCriteriaForm = form.save()
		my_profile.myCriteria = myCriteriaForm
		my_profile.save()
	context = {"myprofile":my_profile,"form":form}
	return render(request,'my_criteria.html',context)	





def handle_uploaded_file(f,filename):
	os_path = os.path.join(os.path.dirname(settings.BASE_DIR),"shroomme_dio","static","photos",filename)
	with open(os_path, 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)
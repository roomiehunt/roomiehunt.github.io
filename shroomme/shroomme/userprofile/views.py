from django.shortcuts import render,Http404,redirect,render_to_response
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import ProfileForm,SearchForm,EditForm,UploadProfileImage,NewUserForm
from shroomme.forms import LoginForm,SignUpForm
from django.http import JsonResponse

#-----------------------------------MODELS-------------------------#
import pprint 
from django.contrib.auth.models import User
from .models import Profile
from django.db.models import Q
from django.forms.models import model_to_dict
from friends.models import Friends,getStatus,getFriendsObject
from constants.constants import constants,gethome
from notification.models import Notification
from roomate.forms import CriteriaForm
from roomate.models import Roomate
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
		return render(request,'profile.html',context)
	else:
		return render(request,'profile.html',{})	
#		return redirect(gethome())


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

def new_user(request):
	form = NewUserForm()
	my_Criteria_form = CriteriaForm()
	search_criteria_form = CriteriaForm()
	slider_attributes = ["cleanliness","sleeping_habit","drinking","noisiness","overnight_guests","cooking"]

#	slider_attributes = [("cleanliness","messy","clean"),("sleeping_habit","morning","night")]

	checkbox_attributes = ["smoke","pet"]

	context = {"my_Criteria_form":my_Criteria_form,"search_criteria_form":search_criteria_form,"form":form}
	context.update({"slider_attributes":slider_attributes})
	return render(request,'new_user.html',context)


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
		if request.method == 'GET':
			print request.GET
			if len(request.GET) == 0:
				return render(request,'find_people.html',{})
			else:
				keys = []
				values = []
				q_objects = []
				positive_main_value_attributes =  ["cleanliness"]
				negative_main_value_attributes =  ["sleeping_habit","drinking","noisiness","overnight_guests","cooking","budget"]
				main_string_attributes = ["smoke","pet","gender"]
				plus_point_attributes = ["major","hobby"]
				positive_dict = {}
				negative_dict = {}
				string_dict = {}
				my_key =0
				my_value = 0
				nationality_dict = {}
				#--Q MODEL PROCESSING
				for key in request.GET.iterkeys():
					my_key = key.lower()
					my_value = request.GET[key]
					if my_key == "nationality":
						nationality_dict = {my_key:my_value}
						temp_Q = Q(**nationality_dict)
					elif my_key in positive_main_value_attributes:
						tag = "myCriteria__" + my_key + "__gte"
						integer_value = int(my_value)
						my_q = Q(**{tag:integer_value})
						q_objects.append(my_q)
					elif my_key in negative_main_value_attributes:
						tag = "myCriteria__" + my_key + "__lte"
						integer_value = int(my_value)
						my_q = Q(**{tag:integer_value})
						q_objects.append(my_q)
					elif (my_key in main_string_attributes) or (my_key in plus_point_attributes):
						tag = "myCriteria__" + my_key 
						my_q = Q(**{tag:my_value})
						q_objects.append(my_q)
				query_text = request.GET["university"]
				query_split = query_text.split(" ")
				q_univ = Q(university__startswith = query_text)
				q_first_name = Q(first_name__startswith = query_text)
				q_last_name = Q(last_name__startswith = query_text)
				q_starts_with = ( q_univ | q_first_name | q_last_name )				
				if len(query_split) == 2:
					q_first_name_2 = Q(first_name__startswith = query_split[0])
					q_last_name_2 = Q(last_name__startswith = query_split[1])
					q_starts_with = ( q_univ | q_first_name | q_last_name | q_first_name_2 | q_last_name_2)				
				q_nationality = Q(**nationality_dict)
				q_final = Q(myCriteria__cleanliness__gte = 0)
				for elem in q_objects:
					q_final = q_final & elem
				final_result = Profile.objects.filter(q_starts_with,q_nationality,q_final)				
				context = {"result":final_result}
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
			#------------------------------FRIENDS CODE----------------------------------------#
			friends_object12 = Friends.manager.get_object_from(user1_uuid,user2_uuid)
			friends_object21 = Friends.manager.get_object_from(user2_uuid,user1_uuid)
			if friends_object12 is not None:
				if friends_object21 is not None:
					if friends_object12.status == "I" and friends_object21.status =="I":
						context.update( {"interest":"mutual","roomate_id":"none"} )
				else:
					if friends_object12.status == "I":
						context.update({"interest":"pending"})
			else:
				if friends_object21 is not None:
					if friends_object21.status == "I":
						context.update({"interest":"interested"})
			#------------------------------FRIENDS CODE----------------------------------------#
			#------------------------------ROOMATE CODE----------------------------------------#
			roomate_object = Roomate.manager.get_object_from(user1_uuid,user2_uuid)
			print roomate_object			
			if roomate_object is not None:
				roomate_status = roomate_object.status
				if roomate_status == 'P': #--PENDING
					if user1_uuid == roomate_object.user1_uuid:
						context.update({"interest":"roomate_waiting","roomate_id":"none"})	
					else:
						context.update({"interest":"roomate_pending","roomate_id":roomate_object.roomate_id})
				elif roomate_status == 'R': #--ROOMATES
					context.update({"interest":"roomates"})


			#------------------------------ROOMATE CODE----------------------------------------#
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
			print context
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


#-------------AJAX------------------------#
#-------------AJAX------------------------#
#-------------AJAX------------------------#
#-------------AJAX------------------------#
#-------------AJAX------------------------#
#-------------AJAX------------------------#
#-------------AJAX------------------------#
def search_name(request):
	if request.is_ajax() and request.method == "POST":
		query = request.POST['query']
		q1 = Q(first_name__startswith=query)
		q2 = Q(last_name__startswith=query)
		result = Profile.objects.filter( (q1 or q2) )[:5]
		json_list = []
		for elem in result.iterator():
			json_list.append(elem.first_name + " " + elem.last_name)
		return JsonResponse(json_list,safe=False)
	else:
		return render(request,'../test/',{})			
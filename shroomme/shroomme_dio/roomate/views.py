from django.shortcuts import render
from userprofile.models import Profile
from .forms import CriteriaForm
from .models import Criteria,Roomate
from notification.models import Notification

def criteria_view(request):
	currentUser = Profile.objects.get(user=request.user)
	form = CriteriaForm(request.POST or None , instance = currentUser.searchCriteria or None)

	if request.method == "POST":
		if form.is_valid():
			print request.POST
			searchCriteriaForm = form.save()
			currentUser.searchCriteria = searchCriteriaForm
			currentUser.save()
	#roomate_list = Roomate.manager.getRoomates(request.user);
	#print roomate_list
			 
	context ={'form':form}	
	return render(request,'roomate.html',context)


def match_result(request):
	userlist = Profile.objects.all()
	this_user = Profile.objects.get(user = request.user)
	result = []
#	positive_main_value_attributes =  ["cleanliness","sleeping_habit","drinking","noisiness","overnight_guests","cooking","budget"]	
	positive_main_value_attributes =  ["cleanliness"]
	negative_main_value_attributes =  ["sleeping_habit","drinking","noisiness","overnight_guests","cooking","budget"]
	main_string_attributes = ["smoke","pet","gender"]
	plus_point_attributes = ["major","hobby"]
	totalScore = len(plus_point_attributes) + len(positive_main_value_attributes)
	#-----------------------SCORE CALCULATION-------------------------#
	#------------------------------------------------------------------
	mySearch =  this_user.searchCriteria			
	mySearch = vars(mySearch)
	myCriteria = this_user.myCriteria
	myCriteria = vars(myCriteria)		

	for elem in userlist:
		if elem.searchCriteria is None or elem.myCriteria is None:
			continue
		if elem == this_user:
			continue
		myScore = 0		#my search their criteria
		otherScore = 0	#their search my criteria
		otherSearch = elem.searchCriteria
		otherSearch = vars(otherSearch)
		otherCriteria = elem.myCriteria
		otherCriteria = vars(otherCriteria)
		flag = 0

		for e1 in main_string_attributes:
			if mySearch[e1] == "any" or otherCriteria == "any":
				continue

			if mySearch[e1] == "U" or otherCriteria == "U":
				continue

			if mySearch[e1] != otherCriteria[e1]:
				print "first"
				flag = 1
				break
			if otherSearch[e1] != myCriteria[e1]:
				print otherSearch[e1]
				print myCriteria[e1]				
				flag = 1
				break

		if flag == 1:
			print "FLAGG_FAIL___________"
			continue

		for e1 in positive_main_value_attributes:
			if mySearch[e1] >= otherCriteria[e1]:
				myScore+=1
			if otherSearch[e1] >= myCriteria[e1]:
				otherScore+=1

		for e1 in negative_main_value_attributes:
			if mySearch[e1] >= otherCriteria[e1]:
				myScore+=1
			if otherSearch[e1] >= myCriteria[e1]:
				otherScore+=1

		for e1 in plus_point_attributes:
			if mySearch[e1] == otherCriteria[e1]:
				myScore+=1
			if otherSearch[e1] == myCriteria[e1]:
				otherScore+=1

		if myScore > 5 and otherScore > 5:
			print "MATCH SCORE-----------------" + str(myScore)
			tuple_result = elem
			result.append(elem)
			print result
		if len(result) == 10:
			break
	#------------------------------------------------------------------
	#------------------------------------------------------------------
	print Roomate.manager.getMyRoomates(this_user.id)

	context = {"result":result}
	return render(request,'match_result.html',context)


#---ajax----#
def add_roomate(request):
	print "ADD_ROOMATE"

	if request.method == "POST" and request.is_ajax():
		print "AJAX----ADD_ROOMATE"
		context = {}
		user1 = request.user
		user1_profile = Profile.objects.get(user=user1)		
		user1_uuid = user1_profile.id
		user2_uuid = request.POST['user2_uuid']
		user2_profile = Profile.objects.get(id=user2_uuid)
		user2 = user2_profile.user
		roomate_object = Roomate(user1=user1,user2=user2,status = "P",user1_uuid=user1_uuid,user2_uuid=user2_uuid)
		roomate_object.save()
		message = user1_profile.first_name + " " + user1_profile.last_name + " wants to be roomates with you"
		notification_object = Notification(
											user1=user1,
											user2=user2,
											message=message,
											read=False,
											notification_type="FR",
											target_id=roomate_object.roomate_id,
											user1_uuid=user1_uuid,
											user2_uuid=user2_uuid)
		notification_object.save()					
		print user2_uuid;
		return render(request,'error.html',context)


	return render(request,'error.html',{})




#------ajax----#
def change_roomate_status(request):
	return render(request,'error.html',{})


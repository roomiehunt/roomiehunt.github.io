from django.shortcuts import render
from userprofile.models import Profile
from .forms import CriteriaForm
from .models import Criteria,Roomate

def criteria_view(request):
	currentUser = Profile.objects.get(user=request.user)
	form = CriteriaForm(request.POST or None , instance = currentUser.searchCriteria or None)

	if request.method == "POST":
		if form.is_valid():
			print "NEED TO PROCESS CRITERIA FORM---------------"
			print request.POST
			searchCriteriaForm = form.save()
			currentUser.searchCriteria = searchCriteriaForm
			currentUser.save()
		 
	context ={'form':form}
	return render(request,'roomate.html',context)


def match_result(request):
	userlist = Profile.objects.all()
	this_user = Profile.objects.get(user = request.user)
	result = []
	positive_main_value_attributes =  ["cleanliness","sleeping_habit","drinking","noisiness","overnight_guests","cooking","budget"]
	#negative_main_value_attributes =  ["drinking","noisiness","overnight_guests","cooking","budget"]	
	main_string_attributes = ["smoke","pet","gender"]
	plus_point_attributes = ["major","hobby"]
	totalScore = len(plus_point_attributes) + len(main_string_attributes) + len(positive_main_value_attributes)
	#-----------------------SCORE CALCULATION-------------------------#
	#------------------------------------------------------------------
	for elem in userlist:
		if elem == this_user:
			continue
		if elem.myCriteria is not None:
			otherUser =  elem.myCriteria;#			
			search = this_user.searchCriteria;
			score = 0
			otherUser = vars(otherUser)
			search = vars(search)
#			print dir(search)			
#			print vars(search)
			for e1 in positive_main_value_attributes:
				if otherUser[e1] >= search[e1]:
					score+=1;

			for e2 in main_string_attributes:
				if otherUser[e2] == search[e2]:
					score+=1;

			for e3 in plus_point_attributes:
				if otherUser[e3] == search[e3]:
					score+=1;			
			
			if score > 5:
				print "MATCH SCORE-----------------" + str(score)
				tuple_result = elem
				result.append(tuple_result)
				print result
		if len(result) == 10:
			break
	#------------------------------------------------------------------
	#------------------------------------------------------------------
	print Roomate.manager.getMyRoomates(this_user.id)

	context = {"result":result}
	return render(request,'match_result.html',context)
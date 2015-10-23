from django.shortcuts import render
from userprofile.models import Profile
from .forms import CriteriaForm

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
	acceptance = 1
	userlist = Profile.objects.all()
	this_user = Profile.objects.get(user = request.user)
	result = []
	for elem in userlist:
		match = 0
		if elem == this_user:
			continue
		print elem.userCriteria
		if elem.userCriteria is not None:
			otherUser =  elem.userCriteria;#			
			myUser = this_user.searchCriteria;
			if otherUser.cleanliness == myUser.cleanliness:
				print "SAME-----------------------------------"
				result.append(elem)
				print result

			#for field in (elem.userCriteria)._meta.get_all_field_names():
			#	print field 

#			if same:
#				result.append(elem)


	context = {"result":result}
	return render(request,'match_result.html',context)
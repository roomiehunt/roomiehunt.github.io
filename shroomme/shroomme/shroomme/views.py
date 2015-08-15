from django.shortcuts import render,Http404,redirect,render_to_response,HttpResponseRedirect
from .forms import NameForm,LoginForm,SignUpForm
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from userprofile.models import Profile
from django.db import IntegrityError
import userprofile.views as userprofileviews

def home(request):
	if request.user.is_authenticated():
		#return HttpResponseRedirect('/myprofile/') 
		return redirect(userprofileviews.myprofile)

	login_form = LoginForm()
	signup_form = SignUpForm()
	message = "none"
	context = {'login':login_form,'signup':signup_form,'message':message}    

	if request.method == 'POST':
		login_form = LoginForm(request.POST)
		signup_form = SignUpForm(request.POST)
		#print request.POST
		if 'signup' in request.POST and signup_form.is_valid(): #------------------------------------------------------IF SIGN UP FORM-----------------------#
			username = signup_form.cleaned_data['username']
			password = signup_form.cleaned_data['password']
			print "--------------------------------SIGN UP FORM-------------------------------------------"
			print username
			print password
#			login_form = LoginForm()
#			signup_form = SignUpForm()
			#TRY TO SIGN UP
			try:
				User.objects.create_user(username, username, password)
				user = authenticate(username=username,password=password)
				login(request,user)
				if user is not None:
					print "PASS"
					print user
				newprofile = Profile(user = user)
				newprofile.save()
				return redirect(userprofileviews.first_time_user)	
			except IntegrityError as e:				#------------------------------WRONG ERROR-----------------------------------#
				context = {'login':login_form,'signup':signup_form,'message':e.__cause__}    
				return render_to_response("error.html", context)
		elif 'login' in request.POST and login_form.is_valid(): #--------------------------------------IF LOGIN FORM-------------------------------$
			username = login_form.cleaned_data['username']
			password = login_form.cleaned_data['password']
			print "--------------------------------LOGIN FORM-------------------------------------------"
			print username
			print password
			login_form = LoginForm()
			signup_form = SignUpForm()			
			user = authenticate(username=username, password=password)
			if(user is not None):
				if(user.is_active):
					login(request,user)
					return HttpResponseRedirect('/myprofile/') 
				else:
					print "user_not_active"

		else:
			login_form = LoginForm()
			signup_form = SignUpForm()

	return render(request,'index.html',context);


def logout_view(request):
	logout(request)
	return redirect(home)

			
def navbar(request):
	return render(request,'navbar\\navbar.html',{});

def first_time_user(request):
	return render(request,'first-time-user.html',{});

def test(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
        	name = form.cleaned_data['name']
        	print name
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
    else:
	    form = NameForm()
    context = {'form':form}
    return render(request,'test\\test.html',context);
			
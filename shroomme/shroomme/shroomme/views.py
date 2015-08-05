from django.shortcuts import render,Http404,redirect
from .forms import NameForm,LoginForm,SignUpForm
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(request):
	login_form = LoginForm()
	signup_form = SignUpForm()
	context = {}
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		login_form = LoginForm(request.POST)
		signup_form = SignUpForm(request.POST)
		# check whether it's valid: >>>>>>>>>>>> IF SIGN UP FORM IS VALID CREATE USER
		if signup_form.is_valid():
			username = signup_form.cleaned_data['username']
			password = signup_form.cleaned_data['password']
			email = signup_form.cleaned_data['email']
			print "--------------------------------SIGN UP FORM-------------------------------------------"
			print username
			print password
			print email
			login_form = LoginForm()
			signup_form = SignUpForm()
			User.objects.create_user(username, email, password)
		elif login_form.is_valid():
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
					return redirect(login_view)
				else:
					print "user_not_active"

		else:
			login_form = LoginForm()
			signup_form = SignUpForm()

	context = {'login':login_form,'signup':signup_form}    
	return render(request,'index.html',context);
			

def logout_view(request):
	logout(request)
	return redirect(home)


def navbar(request):
	return render(request,'navbar\\navbar.html',{});

def userprofile(request):
	return render(request,'userprofile.html',{});

def first_time_user(request):
	return render(request,'first-time-user.html',{});

@login_required(login_url='/')
def login_view(request):
	#context = {'username':username}
	return render(request,'login.html',{});

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
			
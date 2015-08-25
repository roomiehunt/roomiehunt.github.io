from django.shortcuts import render

# Create your views here.
def show_messaging(request):
	context = {}
	return render(request,"show_messaging.html",{})
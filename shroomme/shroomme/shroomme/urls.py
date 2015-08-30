"""shroomme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = [

    #---------------NON - AUTHENTICATED URLS ---------------------------------#
    #---------------HOME+ABOUT US + CONTACT US--------------------------------#
    url(r'^$', 'shroomme.views.home',name='shroomme_home'),




    #----------------USER PROFILE +LOGIN + LOGOUT ----------------------------#
    url(r'^logout/$','userprofile.views.logout_view',name='logout'),
    url(r'^myprofile/$','userprofile.views.myprofile',name='myprofile'),
    url(r'^first_time_user/$','userprofile.views.first_time_user',name='first_time_user'),
    url(r'^find_people/$','userprofile.views.find_people',name='find_people'),
    url(r'^show_user/$','userprofile.views.show_user',name='show_user'),
    url(r'^edit_profile/$','userprofile.views.edit_profile',name='edit_profile'),

    #------------------------NOTIFICATION------------------------------------#
    url(r'^notification/$','notification.views.show_notification',name='show_notification'),
    #--------------------------MESSAGING-------------------------------------#
    url(r'^messaging/$','messaging.views.show_messaging',name='show_messaging'),
    url(r'^show_messages/$','messaging.views.show_messages',name='show_messages'),  #---AJAX---#
    url(r'^create_messages/$','messaging.views.create_messages',name='create_messages'), #---AJAX--#
    
    #--------------------------FRIENDS-----------------------------------#
    url(r'^show_friends/$','friends.views.show_friends',name='show_friends'),
    url(r'^add_friend/$','friends.views.add_friend',name='add_friend'), #---AJAX--#
    url(r'^change_friend_status/$','friends.views.change_friend_status',name='change_friend_status'), #---AJAX---#


    #--------------------FOR TESTING------------------------------------------#
    url(r'^navbar/$', 'shroomme.views.navbar',name='navbar'),
    url(r'^test/$', 'shroomme.views.test',name='test'),# 127.0.0.1:8000/test
    url(r'^admin/', include(admin.site.urls)),
    #----------------------------------FOR TESTING----------------------------#
]


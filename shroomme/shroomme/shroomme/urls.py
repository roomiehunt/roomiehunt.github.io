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

urlpatterns = [

    #---------------NON - AUTHENTICATED URLS ---------------------------------#
    #---------------HOME+ABOUT US + CONTACT US--------------------------------#
    url(r'^$', 'shroomme.views.home',name='shroomme_home'),




    #----------------AUTHENTICATED URLS---------------------------------------#
    #----------------USER PROFILE +LOGIN + LOGOUT ----------------------------#
    url(r'^logout/$','userprofile.views.logout_view',name='logout'),
    url(r'^myprofile/$','userprofile.views.myprofile',name='myprofile'),
    url(r'^first_time_user/$','userprofile.views.first_time_user',name='first_time_user'),
    url(r'^find_people/$','userprofile.views.findpeople',name='find_people'),
    url(r'^show_user/$','userprofile.views.show_user',name='show_user'),

    #----------------USER PROFILE +LOGIN + LOGOUT ----------------------------#



    #--------------------FOR TESTING------------------------------------------#
    url(r'^navbar/$', 'shroomme.views.navbar',name='navbar'),
    url(r'^test/$', 'shroomme.views.test',name='test'),
    url(r'^admin/', include(admin.site.urls)),
    #----------------------------------FOR TESTING----------------------------#
]

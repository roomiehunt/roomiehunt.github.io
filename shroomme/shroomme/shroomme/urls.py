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
    url(r'^$', 'shroomme.views.home',name='home'),
    url(r'^login/$','shroomme.views.login_view',name='login'),
    url(r'^logout/$','shroomme.views.logout_view',name='logout'),

    url(r'^first_time_user/$','shroomme.views.first_time_user',name='first_time_user'),
    url(r'^myprofile/$','shroomme.views.userprofile',name='userprofile'),
    url(r'^navbar/$', 'shroomme.views.navbar',name='navbar'),
    url(r'^test/$', 'shroomme.views.test',name='test'),
    url(r'^admin/', include(admin.site.urls)),
]

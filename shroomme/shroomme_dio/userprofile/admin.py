from django.contrib import admin
from .models import Profile

# Register your models here.
#class profileAdmin(admin.ModelAdmin):

class ProfileAdmin(admin.ModelAdmin):
	model = Profile
	list_display = ('user', 'first_name','last_name','university','id','private','profile_image')
	def get_name(self, obj):
		return obj.Profile.user
	get_name.admin_order_field  = 'user'  #Allows column order sorting
	get_name.short_description = 'users'  #Renames column head



admin.site.register(Profile, ProfileAdmin)

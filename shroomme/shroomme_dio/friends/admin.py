from django.contrib import admin
from .models import Friends
# Register your models here.



class FriendsAdmin(admin.ModelAdmin):
	model = Friends
	list_display = ('user1', 'user2','status','user1_uuid','user2_uuid')
	def get_name(self, obj):
		return obj.Friends.user1
	get_name.admin_order_field  = 'user1'  #Allows column order sorting
	get_name.short_description = 'users'  #Renames column head

admin.site.register(Friends,FriendsAdmin)
from django.contrib import admin
from .models import Notification
# Register your models here.


class NotificationAdmin(admin.ModelAdmin):
	model = Notification
	list_display = ('user1', 'user2','target_id','notification_type','message','read','user1_uuid','user2_uuid')
	def get_name(self, obj):
		return obj.Notification.user1
	get_name.admin_order_field  = 'user1'  #Allows column order sorting
	get_name.short_description = 'users'  #Renames column head


admin.site.register(Notification,NotificationAdmin)
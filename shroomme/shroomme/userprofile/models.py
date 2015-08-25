from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.conf import settings
from constants.constants import constants
import uuid,os
# Create your models here.





def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Profile(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.OneToOneField(settings.AUTH_USER_MODEL,blank = False,null = False)	#user_id --> in dictionary
	first_name = models.CharField(max_length=50,blank=False,null=False,default = "Unspecified")
	middle_name = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
	last_name = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
	nationality = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
	university = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
	gender = models.CharField(max_length=1,choices=constants.GENDER_CHOICES,default='U')
	private = models.BooleanField(default = False)
	roomate_status = models.CharField(max_length=1,choices=constants.ROOMATE_STATUS,default='U')
	roomate_number = models.IntegerField(default=0)
	
#	profile_image = ImageField(upload_to=get_image_path, blank=True, null=True)

    #profile_image = ImageField(upload_to=get_image_path, blank=True, null=True)
#	middle_name = models.TextField(null=True,blank=True)

# class ProfileNew(AbstractUser):
# 	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
# 	user = models.OneToOneField(settings.AUTH_USER_MODEL,blank = False,null = False)	#user_id --> in dictionary
# 	first_name = models.CharField(max_length=50,blank=False,null=False,default = "Unspecified")
# 	middle_name = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
# 	last_name = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
# 	nationality = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
# 	university = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
# 	gender = models.CharField(max_length=1,choices=constants.GENDER_CHOICES,default='U')
# 	private = models.BooleanField(default = False)
# 	roomate_status = models.CharField(max_length=1,choices=constants.ROOMATE_STATUS,default='U')
# 	roomate_number = models.IntegerField(default=0)

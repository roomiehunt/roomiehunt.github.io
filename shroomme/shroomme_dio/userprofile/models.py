from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.conf import settings
from constants.constants import constants
from roomate.models import Criteria
import uuid,os
# Create your models here.



def upload_location(instance, filename):
	#extension = filename.split(".")[1]
	location = str(instance.id)
	return "%s/%s" %(location, filename)

def get_image_path(instance, filename):
	return os.path.join('static', 'photos')

def emptyCriteria():
	return Criteria(




		)


class Profile(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.OneToOneField(settings.AUTH_USER_MODEL,blank = False,null = False)	#user_id --> in dictionary
	first_name = models.CharField(max_length=50,blank=False,null=False,default = "Unspecified")
	middle_name = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
	last_name = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
	nationality = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
	university = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
	gender = models.CharField(max_length=1,choices=constants.GENDER_CHOICES,default='M')
	private = models.BooleanField(default = False)
	profile_image = models.ImageField(upload_to=upload_location,default = "76de327c-16ed-492b-ae9e-8ff6ca36af65/apple.jpg")
	searchCriteria = models.ForeignKey(Criteria,blank = True,null = True,related_name="criteria+")
	myCriteria = models.ForeignKey(Criteria,blank = True ,null = True)

#	move_in_date = models.
#	duration = models.
#class ProfileCriteria(models.Model):
# Profile picture (top left)
# First name*

# Last name*

# Username

# University/School/College* (dropdown with suggestion/auto search)

# Email*

# Status* (looking for a roommate/ looking for a roommate and a place)

# Move in date*

# Gender* (dropdown)

# Age

# Nationality* 

# Major

# Smoker/ non-smoker (checkbox)*

# Hobby/interest: list of sports/sport team, music/bands, 

# Pet/ no-pet* (checkbox)

# Relationship status*

# Cleanliness* (in scale, clean to messy)

# Sleeping habits* (in scale, early to really late/no sleep)

# Drinking* (in scale, never to drink regularly)

# Noisiness* (in scale)

# Guests coming* (in scale, never to all the time)

# Overnight guests? (Y/N)

# Cooking* (in scale, never to regularly)

# Budget (in range?? not sure if we need one)












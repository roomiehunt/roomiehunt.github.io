from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.conf import settings
from constants.constants import constants
import uuid,os

# Create your models here.

class Criteria(models.Model):
	user_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
	#---CHAR FIELD-----_#
	major = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
	hobby = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
	#-----CHOICES---------#
	smoke = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
	pet = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
	relationship_status = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
	gender = models.CharField(max_length=1,choices=constants.GENDER_CHOICES,default='U')
	nationality = models.CharField(max_length=50,null=True,blank=True,default = "Unspecified")
	#------SCALE----------#
	cleanliness = models.IntegerField(choices= constants.LEVEL,default = 0)	
	sleeping_habit = models.IntegerField(choices= constants.LEVEL,default = 0)
	drinking = models.IntegerField(choices= constants.LEVEL,default = 0)
	noisiness = models.IntegerField(choices= constants.LEVEL,default = 0)
	overnight_guests = models.IntegerField(choices= constants.LEVEL,default = 0)
	cooking = models.IntegerField(choices= constants.LEVEL,default = 0)
	budget = models.IntegerField(default = 0)




#class Roomate(models.Model):



# Gender* (men/women/either)

# Age

# Nationality (any by default unless user have preferences)

# Major

# Smoker/ non-smoker (checkbox)*

# Hobby/interest

# Pet/ no-pet* (checkbox)

# Relationship status* (dropdown menu, only single/ ok with any)

# Cleanliness* (in scale, clean to messy)

# Sleeping habits* (in scale, early to late/no sleep)

# Drinking* (in scale, never to drink regularly)

# Noisiness* (in scale)

# Guests coming* (in scale, never to all the time)

# Overnight guests? (Y/N)

# Cooking* (in scale, never to regularly)

# Budget (in range?? not sure if we need one)
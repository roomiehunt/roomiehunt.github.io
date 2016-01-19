from django.forms import ModelForm
from django import forms
from .models import Profile
from constants.constants import constants
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from crispy_forms.bootstrap import FormActions
from constants.constants import constants


class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['first_name', 'middle_name', 'last_name','nationality','gender','private']

	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.layout.append(
			FormActions(
			HTML("""<a class="btn btn-default"
			href="{% url "myprofile" %}">Skip</a>"""),
			HTML("&nbsp&nbsp&nbsp"),
			Submit('submit', 'Submit'),
	))



class NewUserForm(ModelForm):
	class Meta:
		model = Profile
		exclude = ['id','user','searchCriteria','userCriteria']



class EditForm(ModelForm):
	class Meta:
		model = Profile
		exclude = ['id','user','searchCriteria','userCriteria']


class SearchForm(forms.Form):
	university = forms.CharField(label='', max_length=1000,required=False)
	roomate_status = forms.ChoiceField(choices=constants.ROOMATE_STATUS)
	#roomate_number = forms.IntegerField(min_value = 0,max_value = 4,initial=0)

# class UploadProfileImage(forms.Form):
# 	user_image = forms.ImageField(label = '')


class UploadProfileImage(ModelForm):
	class Meta:
		model = Profile
		fields = ['profile_image']	


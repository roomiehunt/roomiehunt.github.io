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

	# user = models.OneToOneField(settings.AUTH_USER_MODEL,primary_key = True,blank = False,null = False)
	# first_name = models.TextField(null=True,blank=True)
	# middle_name = models.TextField(null=True,blank=True)
	# last_name =  models.TextField(null=True,blank=True)
	# nationality = models.TextField(null=True,blank=True)
	# gender = models.TextField(choices=GENDER_CHOICES,default='U')
class EditForm(forms.Form):
	edit_first_name= forms.CharField(label='', max_length=1000,required=False)
	user_image = forms.FileField()


class SearchForm(forms.Form):
	university = forms.CharField(label='', max_length=1000,required=False)
	roomate_status = forms.ChoiceField(choices=constants.ROOMATE_STATUS)
	roomate_number = forms.IntegerField(min_value = 0,max_value = 4,initial=0)





from django.forms import ModelForm
from django import forms
from .models import Criteria
from userprofile.models import Profile
from constants.constants import constants
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from crispy_forms.bootstrap import FormActions
from constants.constants import constants

class CriteriaForm(ModelForm):
	class Meta:
		model = Criteria
		exclude = ['user_uuid']
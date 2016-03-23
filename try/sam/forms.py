from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import userprofile

class regform(ModelForm):
	#retype_password = forms.CharField(max_length=20,widget=django.PasswordInput)
	class Meta:
		model = User
		fields = ['username','password','email','first_name','last_name']

class profileform(ModelForm):
	class Meta:
		model = userprofile
		exclude = ['user']

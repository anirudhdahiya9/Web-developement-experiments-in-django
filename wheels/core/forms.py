from django import forms
from .models import bike

class RegBike(forms.ModelForm):
	class Meta:
		model = bike
		fields = ['bikemodel','size','date_deployed']

class mylogin(forms.Form):
	username = forms.CharField(label='Username', max_length=50)
	password = forms.CharField(label='Password',widget = forms.PasswordInput,max_length=20)

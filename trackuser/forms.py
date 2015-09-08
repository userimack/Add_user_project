from django import forms
from trackuser.models import Create,Profile,Post



class NameForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = Create
		fields = ['email','username','password']


class LoginForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput())

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['full_name','address','phone_number']





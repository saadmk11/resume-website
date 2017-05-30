from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")

		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("User Does Not Exist.")
			if not user.check_password(password):
				raise forms.ValidationError("Password Does not Match.")
			if not user.is_active:
				raise forms.ValidationError("User is not Active.")

		return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	confirm_password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ("username", "password", "confirm_password")

	def clean_confirm_password(self):
		password = self.cleaned_data.get("password")
		confirm_password = self.cleaned_data.get("confirm_password")

		if password != confirm_password:
			raise forms.ValidationError("Passwords Must Match")
		return password



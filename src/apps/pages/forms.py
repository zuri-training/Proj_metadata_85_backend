from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class RegisterForm(forms.Form):
	email = forms.EmailField(label='email', widget=forms.TextInput(attrs={'id': 'email'}))
	password =	forms.CharField(label='password', max_length=200, widget=forms.TextInput(attrs={'id': 'password'}))

#-------metadata form----#
class FileUpload(forms.Form):
    upload_file = forms.FileField()


# class NewUserForm(UserCreationForm):
# 	email = forms.EmailField(required=True)

# 	class Meta:
# 		model = User
# 		# fields = ("username", "email", "password1", "password2")
# 		fields = ("email", "password")

# 	def save(self, commit=True):
# 		user = super(NewUserForm, self).save(commit=False)
# 		user.email = self.cleaned_data['email']
# 		if commit:
# 			user.save()
# 		return user

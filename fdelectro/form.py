from django import forms
from . import models


class signinForm(forms.ModelForm):
	class Meta:
		model=models.signin
		fields="__all__"
		
class registerForm(forms.ModelForm):
	class Meta:
		model=models.register
		fields="__all__"

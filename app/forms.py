from django import forms
from .models import *

class eventform(forms.ModelForm):
	class Meta():
		model=event;
		fields='__all__'
	

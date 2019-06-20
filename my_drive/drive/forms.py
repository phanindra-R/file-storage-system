from django import forms
from .models import files

class fileform(forms.ModelForm):
	class Meta:
		model = files
		fields = ('file',)
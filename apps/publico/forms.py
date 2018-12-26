
#encoding:utf-8
from django import forms
from .models import *

class FileUploadForm(forms.ModelForm):

    class Meta:
        model = FileUpload
        exclude = []			


			

	
	
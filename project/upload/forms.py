from django import forms
from django.contrib.auth.models import User
from project.upload.models import Document,Report

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('name', 'document',)

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('email','message')

      
        

from django import forms
from .models import Project,Profile

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','profile']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

from django import forms
from .models import RepoModel

class RepoForm(forms.ModelForm):
   photo = forms.URLField(required=True)
   project_title = forms.CharField(max_length=150, required=True)
   project_description = forms.CharField(widget=forms.TextInput, required=True)
   tags = forms.CharField(required=True)
   github_url = forms.URLField(required=True, initial='https://github.com/')

   class Meta:
      model = RepoModel
      fields = ['photo', 'project_title', 'project_description', 'tags', 'github_url']
      labels = {'photo': 'Photo', 'project_title': 'Project title', 'tags': 'Tags', 'github_url': 'GitHub URL'}

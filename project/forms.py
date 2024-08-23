from django import forms
from  gear1.models import Project

class ProjectForm(forms.Form):
    class Meta:
        model = Project
        fields =['text','photo']
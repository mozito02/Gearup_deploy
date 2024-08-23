from django import forms
from django.forms import TextInput,NumberInput,FileInput
from  gear1.models import Project
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import  User

# class ProjectForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         fields =['participant_no','text','photo']

    
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['participant_no','text','photo']
        widgets = {
            'participant_no': NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Participant Number'
                }),
            'text': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Write brief with link'
                }),
            'photo' :  FileInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Upload photo'
                })

        }


class UserRegistrationForm(UserCreationForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')
    
# class ProjectForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['participant_no','text','photo']
#         widgets = {
#             'participant_no': NumberInput(attrs={
#                 'class': "form-control",
#                 'style': 'max-width: 300px;',
#                 'placeholder': 'Participant Number'
#                 }),
#             'text': TextInput(attrs={
#                 'class': "form-control", 
#                 'style': 'max-width: 300px;',
#                 'placeholder': 'Write brief with link'
#                 }),
#             'photo' :  FileInput(attrs={
#                 'class': "form-control",
#                 'style': 'max-width: 300px;',
#                 'placeholder': 'Upload photo'
#                 })

#         }
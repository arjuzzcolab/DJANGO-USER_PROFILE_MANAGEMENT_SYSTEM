from .models import userProfile,userProject
from django import forms

class userdetailsForm(forms.ModelForm):
    class Meta:
        model = userProfile
        exclude = ['user']
        fields = '__all__'
        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Name'}),
                'about': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tell about Yourself'}),
                'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Email'}),
                'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Country'}),
                'place': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Place'}),
                'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
                'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Age'}),
                'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Contact'}),
                
                'education': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40, 'placeholder': 'Enter your education details here'}),               
        }

class userprojectsForm(forms.ModelForm):
    class Meta:
        model = userProject
        exclude = ['user']
        fields = '__all__'
        widgets = {
                
                'work_experience': forms.NumberInput(attrs={'class': 'form-control', 'rows': 4, 'cols': 40, 'placeholder': 'Enter your work experience here'}),
              
                'skills': forms.TextInput(attrs={'class': 'form-control', 'size': 40, 'placeholder': 'Enter your skills, separated by commas'}),
                'cerifications': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40, 'placeholder': 'Enter your certifications here'}),
                'first_Project_Title': forms.TextInput(attrs={'class': 'form-control', 'size': 40, 'placeholder': 'Enter the project title'}),
                'first_Project_Description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40, 'placeholder': 'Enter the project description'}),
                'first_Project_Image': forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple': False}),
                'first_Project_Link': forms.URLInput(attrs={'class': 'form-control', 'size': 40, 'placeholder': 'Enter the project link'}),
                'second_Project_Title': forms.TextInput(attrs={'class': 'form-control', 'size': 40, 'placeholder': 'Enter the project title'}),
                'second_Project_Description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40, 'placeholder': 'Enter the project description'}),
                'second_Project_Image': forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple': False}),
                'second_Project_Link': forms.URLInput(attrs={'class': 'form-control', 'size': 40, 'placeholder': 'Enter the project link'}),
                'third_Project_Title': forms.TextInput(attrs={'class': 'form-control', 'size': 40, 'placeholder': 'Enter the project title'}),
                'third_Project_Description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40, 'placeholder': 'Enter the project description'}),
                'third_Project_Image': forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple': False}),
                'third_Project_Link': forms.URLInput(attrs={'class': 'form-control', 'size': 40, 'placeholder': 'Enter the project link'}),
                }



from django import forms
from questions.models import MyUser,Questions
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control border border-info","placeholder":"enter username"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control border border-info","placeholder":"enter username"}))
    class Meta:
        model=MyUser
        fields=["first_name","last_name","username","password1","password2","email","phone","profile_pic"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control border border-info","placeholder":"enter firstname"}),
            "last_name":forms.TextInput(attrs={"class":"form-control border border-info","placeholder":"enter lastname" }),
            "username":forms.TextInput(attrs={"class":"form-control border border-info","placeholder":"enter username"}),
            "email":forms.EmailInput(attrs={"class":"form-control border border-info","placeholder":"enter email"}),
            "phone":forms.TextInput(attrs={"class":"form-control border border-info","placeHolder":"enter phone number"})
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info","placeholder":"enter username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control border border-info","placeholder":"enter password"}))

class QuestionForm(forms.ModelForm):
    class Meta:
        model=Questions
        fields=[
            "description",
            "image",
        ]
        widgets={
            "description":forms.Textarea(attrs={"class":"form-control border border-info","rows":4}),
            "image":forms.FileInput(attrs={"class":"form-select border border-info"})

        }
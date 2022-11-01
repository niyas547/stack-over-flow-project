from cProfile import label
from django import forms
from questions.models import MyUser,Questions
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control border border-info","placeholder":"enter password"}),label='')
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control border border-info","placeholder":"confirm password"}),label='')
    first_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info","placeholder":"enter firstname"}),label='')
    last_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info","placeholder":"enter lastname" }),label='')
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info","placeholder":"enter username"}),label='')
    email=forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control border border-info","placeholder":"enter email"}),label='')
    phone=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info","placeHolder":"enter phone number"}),label='')
    profile_pic=forms.FileField(widget=forms.FileInput(attrs={"class":"form-select border border-info",}))
    class Meta:
        model=MyUser
        fields=["first_name","last_name","username","password1","password2","email","phone","profile_pic"]
     

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
            "description":forms.Textarea(attrs={"class":"form-control border border-primary border border-3","rows":4,"placeholder":"what's your question?"}),
            "image":forms.FileInput(attrs={"class":"form-select border border-primary border border-3"})

        }

class AnswerForm(forms.Form):
    answer=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control border border-dark border border-2","rows":5}))
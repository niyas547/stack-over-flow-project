from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from questions.forms import RegistrationForm,LoginForm
from django.views.generic import CreateView,View
from questions.models import MyUser
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from questions.models import MyUser
# Create your views here.

class IndexView(TemplateView):
    template_name="index.html"
   
class SignupView(CreateView):
    model=MyUser
    form_class=RegistrationForm
    template_name="register.html"
    success_url=reverse_lazy("register")

class SigninView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                return redirect("index")
            else:
                return render(request,"login.html",{"form":form})


from urllib import request
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from questions.models import Questions
from questions.forms import RegistrationForm,LoginForm,QuestionForm
from django.views.generic import CreateView,View,FormView,ListView
from questions.models import MyUser
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from questions.models import MyUser
# Create your views here.

   
class SignupView(CreateView):
    model=MyUser
    form_class=RegistrationForm
    template_name="register.html"
    success_url=reverse_lazy("login")

class SigninView(FormView):
    form_class=LoginForm
    template_name="login.html"
    # def get(self,request,*args,**kwargs):
    #     form=LoginForm
    #     return render(request,"login.html",{"form":form})
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

def signout_view(request,*args,**kwargs):   
    logout(request)
    return redirect("login")

class IndexView(CreateView,ListView):
    model=Questions
    form_class=QuestionForm
    template_name="home.html"
    success_url=reverse_lazy("index")
    context_object_name="questions"

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    def get_queryset(self):
        return Questions.objects.all().exclude(user=self.request.user)

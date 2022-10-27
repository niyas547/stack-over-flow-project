


from django.shortcuts import render,redirect
from questions.forms import RegistrationForm,LoginForm,QuestionForm
from django.views.generic import TemplateView,CreateView,View,FormView,ListView,DetailView
from questions.models import Answers, MyUser
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from questions.models import MyUser,Questions
from django.contrib import messages
from django.utils.decorators import method_decorator
# Create your views here.
def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"you must login")
            return redirect("login")
        else:
            return fn(request,*args,**kwargs)
    return wrapper
   
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
                messages.success(request,"Login Completed")
                return redirect("index")
            else:
                messages.error(request,"Invalid Credentials")
                return render(request,"login.html",{"form":form})
@signin_required
def signout_view(request,*args,**kwargs):   
    logout(request)
    return redirect("login")

@method_decorator(signin_required,name="dispatch")
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

class QuestionDetailView(DetailView):
    model=Questions
    template_name="question-detail.html"
    pk_url_kwarg="id"
    context_object_name="question"

def add_answer(request,*args,**kwargs):
    qid=kwargs.get("id")
    question=Questions.objects.get(id=qid)
    answer=request.POST.get("answer")
    Answers.objects.create(user=request.user,answer=answer,question=question)
    return redirect("index")




from django.shortcuts import render,redirect
from questions.forms import RegistrationForm,LoginForm,QuestionForm,AnswerForm
from django.views.generic import TemplateView,CreateView,View,FormView,ListView,DetailView
from questions.models import Answers, MyUser
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from questions.models import MyUser,Questions
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.views.decorators.cache import never_cache
# Create your views here.
def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"you must login")
            return redirect("login")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

decs=[signin_required,never_cache]

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
                # messages.success(request,"Login Completed")
                return redirect("index")
            else:
                messages.error(request,"Invalid Credentials")
                return render(request,"login.html",{"form":form})
decs
def signout_view(request,*args,**kwargs):   
    logout(request)
    return redirect("login")

@method_decorator(decs,name="dispatch")
class IndexView(SuccessMessageMixin,CreateView,ListView):
    model=Questions
    form_class=QuestionForm
    template_name="home.html"
    success_message="Question added Successfully"
    success_url=reverse_lazy("index")
    context_object_name="questions"

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    def get_queryset(self):
        return Questions.objects.all().exclude(user=self.request.user)

@method_decorator(decs,name="dispatch")
class MyquestionsView(View):
    def get(self,request,*args,**kwargs):
        my_questions=request.user.questions_set.all()
        return render(request,"my-questions.html",{"questions":my_questions})
decs
def delete_myquestion(request,*args,**kwargs):
    id=kwargs.get("id")
    Questions.objects.get(id=id).delete()
    return redirect("my-questions")

 

@method_decorator(decs,name="dispatch")
class QuestionDetailView(DetailView,FormView):
    model=Questions
    template_name="question-detail.html"
    pk_url_kwarg="id"
    context_object_name="question"
    form_class=AnswerForm


    


decs
def add_answer(request,*args,**kwargs):
    if request.method=="POST":
        form=AnswerForm(request.POST)
        if form.is_valid():
            answer=form.cleaned_data.get("answer")
            qid=kwargs.get("id")
            question=Questions.objects.get(id=qid)
            Answers.objects.create(question=question,answer=answer,user=request.user)
            return redirect("index")
        else:
            return redirect("add-answer")
decs
def delete_answer(request,*args,**kwargs):
    aid=kwargs.get("id")
    answer=Answers.objects.get(id=aid)
    answer.delete()
    return redirect("index")


# localhost:8000/answers/{id}/upvote
decs
def upvote_view(request,*args,**kwargs):
    ans_id=kwargs.get("id")
    ans=Answers.objects.get(id=ans_id)
    ans.upvote.add(request.user)
    ans.save()
    return redirect("index")
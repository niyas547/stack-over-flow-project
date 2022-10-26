from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    phone=models.CharField(max_length=120)
    profile_pic=models.ImageField(upload_to="profile-pics",null=True)

class Questions(models.Model):
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    description=models.CharField(max_length=120)
    image=models.ImageField(upload_to="images",null=True,blank=True)
    asked_date=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.description

class Answers(models.Model):
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    answer=models.CharField(max_length=120)
    answered_date=models.DateTimeField(auto_now_add=True)
    upvote=models.ManyToManyField(MyUser,related_name="upvote")

    def __str__(self):
        return self.answer

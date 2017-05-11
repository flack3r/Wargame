from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )
    score = models.IntegerField()
    comment = models.CharField(max_length=30, default="")
        
class Board(models.Model):
    autor = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    def publish(self):
        self.save()

class Notice(models.Model):
    notice = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.notice

    def publish(self):
        self.save()


class Problem(models.Model):
    ProbType = models.CharField(max_length=30)
    title = models.CharField(max_length=20)
    Firstblood = models.CharField(max_length=30, null=True)
    text = models.TextField()
    score = models.IntegerField()
    solverNum = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def publish(self):
        self.save()

class Solve(models.Model):
    solver = models.ForeignKey(User, on_delete=models.CASCADE)
    prob = models.ForeignKey(Problem, on_delete=models.CASCADE)

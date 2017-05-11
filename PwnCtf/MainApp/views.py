from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from MainApp.forms import SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as a_login
from MainApp.models import Notice, Problem, Member, Solve
# Create your views here.
def index(request):
    notice = Notice.objects.all().order_by('-created_data')
    return render(request,'index.html', {"Notice": notice})

def login(request):
    if request.method == "POST":
        user_id = request.POST.get('UserName',"")
        passwd = request.POST.get('Password', "")
        
        if user_id == '' or passwd == '':
            return HttpResponse("fail")
        
        user = authenticate(username=user_id, password=passwd)
        if user is not None:
            a_login(request, user)
            return HttpResponse("Suceess")
        else:
            return HttpResponse("fail")
    return HttpResponse("login~")

def register(request):
    if request.method == "POST":
        UserName = request.POST.get('UserName',"")
        Password = request.POST.get('Password',"")
        Email = request.POST.get('Email',"")
        
        if UserName == '' or Password == '' or Email == '':
            return HttpResponse("<script>alert('Register Fail ddd'); history.back(-1); </script>")
        try:
            current_user = User.objects.create_user(username=UserName, email=Email, password = Password)
            member = Member.objects.create(user=current_user, score=0)
            member.save()
            return HttpResponse("<script>alert('Register Ok'); history.back(-1); </script>")
        except:
            return HttpResponse("<script>alert('Register Fail except'); history.back(-1); </script>")

    return HttpResponse("<script>alert('Register Fail'); history.back(-1); </script>")

@login_required(login_url="/PwnCtf/alert/")
def guide(request):
	return render(request,'guide.html',{})

@login_required(login_url="/PwnCtf/alert/")
def problems(request):
	return render(request, 'problems.html', {})

@login_required(login_url="/PwnCtf/alert/")
def Dashboard(request):
	return render(request, 'Dashboard.html', {})

@login_required(login_url="/PwnCtf/alert/")
def Tip(request):
	return render(request, 'Tip.html', {})

def schedule(request):
	return render(request, 'schedule.html', {})

def alert(request):
    return render(request, 'alert.html', {})

def web(request):
    prob = Problem.objects.filter(ProbType='Web')
    solvedList = []
    if request.user.is_authenticated:
        for solved in Solve.objects.filter(solver=request.user):
            solvedList.append(solved.prob.title)

    return render(request, 'web.html', {"Problem": prob, "solvedList": solvedList})
    
def reversing(request):
    prob = Problem.objects.filter(ProbType='Reversing')
    solvedList = []
    if request.user.is_authenticated:
        for solved in Solve.objects.filter(solver=request.user):
            solvedList.append(solved.prob.title)

    return render(request, 'reversing.html', {"Problem": prob, "solvedList": solvedList})

def pwnable(request):
    prob = Problem.objects.filter(ProbType='Pwnable')
    solvedList = []
    if request.user.is_authenticated:
        for solved in Solve.objects.filter(solver=request.user):
            solvedList.append(solved.prob.title)

    return render(request, 'pwnable.html', {"Problem": prob, "solvedList": solvedList})
    
def forensic(request):
    prob = Problem.objects.filter(ProbType='Forensic')
    solvedList = []
    if request.user.is_authenticated:
        for solved in Solve.objects.filter(solver=request.user):
            solvedList.append(solved.prob.title)

    return render(request, 'forensic.html', {"Problem": prob, "solvedList": solvedList})

def crypto(request):
    prob = Problem.objects.filter(ProbType='Crypto')
    solvedList = []
    if request.user.is_authenticated:
        for solved in Solve.objects.filter(solver=request.user):
            solvedList.append(solved.prob.title)

    return render(request, 'crypto.html', {"Problem": prob, "solvedList": solvedList})

@login_required(login_url="/PwnCtf/alert/")
def flagCheck(request):
    flags = {"sql_easy": "PwnCtf{2333BC}", "Caesar": "PwnCtf{rot_1s_so_eas3y}", "bof": "PwnCtf{so_e3sy_bof}", "easy_crack":"PwnCtf{Ea5yR3versing}","easy_stego":"PwnCtf{easy_stego}"}
    if request.method == "POST":
        chal = request.POST.get('challengeName', "")
        input_flag = request.POST.get('flag', "")
    
        if request.user.is_authenticated:
            problems = Problem.objects.get(title=chal)
            if Solve.objects.filter(solver=request.user, prob=problems):
                return HttpResponse("You already solved!")
            else:
                if flags[chal] == input_flag:
                    user = User.objects.get(username=request.user.username)
                    mem = Member.objects.get(user=user)
                    mem.score += problems.score
                    mem.save()
                
                    solver = Solve.objects.create(solver=user, prob=problems)
                    solver.save()

                    problems.solverNum += 1
                    if problems.Firstblood == "null":
                        problems.Firstblood = user.username
                    problems.save()

                    return HttpResponse("Correct")
        else:
            HttpResponse("LoginPlz")

    return HttpResponse("Fail")

def Rank(request):
    temp_list = User.objects.order_by('-member__score')
    rank_list = []
    
    for tmp in temp_list:
        rank_list.append([tmp.username, tmp.member.score, tmp.member.comment])

    return render(request, "rank.html", {"RankList": rank_list})

@login_required(login_url="/PwnCtf/alert/")
def Profile(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user.username)
        password = request.POST.get('password', '')
        comment = request.POST.get('comment','')
        email = request.POST.get('Email', '')
        if password != 'this_is_def3alt_value':
            user.set_password(password)

        mem = Member.objects.get(user=user)
        mem.comment = comment
        mem.save()

        user.email = email
        user.save()
        return HttpResponse("<script>alert('Update Sucees'); window.location.href=\"/\"; </script>")

    return render(request, "profile.html", {})

def Getdone(request, userid):
    user = User.objects.get(username=userid)
    if user:
        solved_list = ""
        solved = Solve.objects.filter(solver=user)
        for tmp in solved:
            solved_list += tmp.prob.title
            solved_list += ","
        
        return HttpResponse("<script>var solved_list = \""+solved_list+"\"; solved_list = solved_list.replace(/,/g,\"\\n\"); alert('===Solved list===\\n'+solved_list); history.back(-1);</script>")
    else:
        return HttpResponse("<script>alert('Wrong Access');</script>")
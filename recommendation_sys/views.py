from django.shortcuts import render, redirect
from .weighted_scoring_model import career_know_skill_personality, career_acad, career_person
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from account.models import student
from personality.models import User_Personality

# Create your views here.


def index(request):
    return render(request, 'recommendation_sys/base.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'])

        if user is not None and student.objects.get(Identification_no=user):
            auth.login(request, user)
            return redirect('studentdashboard')

        else:
            message = 'Incorrect Login Details'
            return render(request, 'recommendation_sys/login.html', {'message': message})
    else:
        return render(request, 'recommendation_sys/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='login')
def studentdashboard(request):
    user = User.objects.get(username=request.user.get_username())
    stud = student.objects.get(Identification_no=user)
    personality = None

    if User_Personality.objects.filter(user_id=stud):
        personality = User_Personality.objects.filter(user_id=stud)

    context = {
        'personality': personality,
        'student': stud,
    }

    return render(request, 'recommendation_sys/studentdashboard.html', context)


@login_required(login_url='login')
def rankings(request):

    u = User.objects.get(username=request.user.get_username())
    person = student.objects.get(Identification_no=u)
    message = ''
    results = None
    record = [0.0 for i in range(6)]

    if User_Personality.objects.filter(user_id=person):
        results = list(User_Personality.objects.filter(
            user_id=person).values())
        record[0] = results[0]['Realistic']
        record[1] = results[0]['Investigative']
        record[2] = results[0]['Artistic']
        record[3] = results[0]['Social']
        record[4] = results[0]['Enterprising']
        record[5] = results[0]['Conventional']

    print(career_acad('0'))
    rankings_KS = career_acad('0')
    rankings_P = career_person('0', record)
    rankings_KSP = career_know_skill_personality('0', record)
    context = {
        "rankings_KS": rankings_KS,
        "rankings_P": rankings_P,
        "rankings_KSP": rankings_KSP,
    }
    return render(request, "recommendation_sys/rankings.html", context)

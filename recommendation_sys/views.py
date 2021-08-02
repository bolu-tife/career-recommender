from django.shortcuts import render, redirect
from .weighted_scoring_model import career_know_skill_personality, career_acad, career_person
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from account.models import student
from personality.models import User_Personality

# Create your views here.


def index(request):
    return render(request, 'recommendation_sys/index.html')

def indexx(request):
    return render(request, 'recommendation_sys/indexx.html')

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
    student_id = str(stud.id-1)
    personality = None

    if User_Personality.objects.filter(user_id=stud):
        personality = User_Personality.objects.filter(user_id=stud)

    context = {
        'personality': personality,
        'student': stud,
        'student_dashboard': 'active',
        'crumb': 'Student Dashboard',
    }

    return render(request, 'recommendation_sys/studentdashboard.html', context)


@login_required(login_url='login')
def rankings(request):

    u = User.objects.get(username=request.user.get_username())
    person = student.objects.get(Identification_no=u)
    student_id = str(person.id-1)
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

    student_id = str(person.id-1)
    # careerdes_KS, rankings_KS = career_acad('0')
    # careerdes_P,rankings_P = career_person('0', record)
    # careerdes_KSP,rankings_KSP = career_know_skill_personality('0', record)

    # careerdes_KS, rankings_KS = career_acad('0')
    # careerdes_P,rankings_P = career_person('0', record)
    # careerdes_KSP,rankings_KSP = career_know_skill_personality('0', record)
    context = {

        
        "rankings_P": career_person(student_id, record)[:2],
        "rankings_KSP": career_know_skill_personality(student_id, record)[:2],
        "rankings_KS": career_acad(student_id)[:2],

        'recomm_career': 'active',
        'crumb': 'Recommend Career',
    }
    return render(request, "recommendation_sys/rankings.html", context)


@login_required(login_url='login')
def rankings_acad(request):

    u = User.objects.get(username=request.user.get_username())
    person = student.objects.get(Identification_no=u)
    student_id = str(person.id-1)
    # results = None
    # record = [0.0 for i in range(6)]

    # if User_Personality.objects.filter(user_id=person):
    #     results = list(User_Personality.objects.filter(
    #         user_id=person).values())
    #     record[0] = results[0]['Realistic']
    #     record[1] = results[0]['Investigative']
    #     record[2] = results[0]['Artistic']
    #     record[3] = results[0]['Social']
    #     record[4] = results[0]['Enterprising']
    #     record[5] = results[0]['Conventional']

    context = {

        "rankings_KS": career_acad(student_id)

    }
    return render(request, "recommendation_sys/rankings_acad.html", context)


@login_required(login_url='login')
def rankings_pers(request):

    u = User.objects.get(username=request.user.get_username())
    person = student.objects.get(Identification_no=u)
    student_id = str(person.id-1)
    results = None
    record = [0.0 for i in range(6)]

    if User_Personality.objects.filter(user_id=person):
        results = list(User_Personality.objects.filter(
            user_id=person).values())
        record[0] = results[0]['Realistic']/5
        record[1] = results[0]['Investigative']/5
        record[2] = results[0]['Artistic']/5
        record[3] = results[0]['Social']/5
        record[4] = results[0]['Enterprising']/5
        record[5] = results[0]['Conventional']/5

    context = {


        "rankings_P": career_person(student_id, record),

    }
    return render(request, "recommendation_sys/rankings_pers.html", context)


@login_required(login_url='login')
def rankings_both(request):

    u = User.objects.get(username=request.user.get_username())
    person = student.objects.get(Identification_no=u)
    results = None
    record = [0.0 for i in range(6)]
    student_id = str(person.id-1)
    if User_Personality.objects.filter(user_id=person):
        results = list(User_Personality.objects.filter(
            user_id=person).values())
        record[0] = results[0]['Realistic']/5
        record[1] = results[0]['Investigative']/5
        record[2] = results[0]['Artistic']/5
        record[3] = results[0]['Social']/5
        record[4] = results[0]['Enterprising']/5
        record[5] = results[0]['Conventional']/5

    context = {

        "rankings_KSP": career_know_skill_personality(student_id, record),

    }
    return render(request, "recommendation_sys/rankings_both.html", context)

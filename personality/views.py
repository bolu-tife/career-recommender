from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import get_form
from .models import User_Personality, Questions
from account.models import student
from django.contrib.auth.models import User
# from django.contrib import messages
import json
from django.http.response import JsonResponse

a = """
[

    {
        "name": "Realistic1",
        "label": "Build kitchen cabinets",
        "type": "radio",
        "choices": [
            {"name": "Strongly Dislike", "value":1},
            {"name": "DisLike", "value":2},
            {"name": "Unsure", "value":3},
            {"name": "Like", "value":4},
            {"name": "Strongly Like", "value":5}
        ]
    },
    {
        "name": "Realistic2",
        "label": "Lay brick or tile",
        "type": "radio",
        "choices": [
            {"name": "Strongly Dislike", "value":1},
            {"name": "DisLike", "value":2},
            {"name": "Unsure", "value":3},
            {"name": "Like", "value":4},
            {"name": "Strongly Like", "value":5}
        ]
    },
    {
        "name": "Investigative1",
        "label": "Develop a new medicine",
        "type": "radio",
        "choices": [
            {"name": "Strongly Dislike", "value":1},
            {"name": "DisLike", "value":2},
            {"name": "Unsure", "value":3},
            {"name": "Like", "value":4},
            {"name": "Strongly Like", "value":5}
        ]
    },
    {
        "name": "Investigative2",
        "label": "Study ways to reduce water pollution",
        "type": "radio",
        "choices": [
            {"name": "Strongly Dislike", "value":1},
            {"name": "DisLike", "value":2},
            {"name": "Unsure", "value":3},
            {"name": "Like", "value":4},
            {"name": "Strongly Like", "value":5}
        ]
    },
    {
        "name": "Artistic1",
        "label": "Write books or plays",
        "type": "radio",
        "choices": [
            {"name": "Strongly Dislike", "value":1},
            {"name": "DisLike", "value":2},
            {"name": "Unsure", "value":3},
            {"name": "Like", "value":4},
            {"name": "Strongly Like", "value":5}
        ]
    },
    {
        "name": "Artistic2",
        "label": "Play a musical instrument",
        "type": "radio",
        "choices": [
            {"name": "Strongly Dislike", "value":1},
            {"name": "DisLike", "value":2},
            {"name": "Unsure", "value":3},
            {"name": "Like", "value":4},
            {"name": "Strongly Like", "value":5}
        ]
    },
    {
        "name": "Social1",
        "label": "Teach an individual an exercise routine",
        "type": "radio",
        "choices": [
            {"name": "Strongly Dislike", "value":1},
            {"name": "DisLike", "value":2},
            {"name": "Unsure", "value":3},
            {"name": "Like", "value":4},
            {"name": "Strongly Like", "value":5}
        ]
    },
    {
        "name": "Social2",
        "label": "Help people with personal or emotional problems",
        "type": "radio",
        "choices": [
            {"name": "Strongly Dislike", "value":1},
            {"name": "DisLike", "value":2},
            {"name": "Unsure", "value":3},
            {"name": "Like", "value":4},
            {"name": "Strongly Like", "value":5}
        ]
    },
    {
        "name": "Enterprising1",
        "label": "Buy and sell stocks and bonds",
        "type": "radio",
        "choices": [
            {"name": "Strongly Dislike", "value":1},
            {"name": "DisLike", "value":2},
            {"name": "Unsure", "value":3},
            {"name": "Like", "value":4},
            {"name": "Strongly Like", "value":5}
        ]
    },
    {
        "name": "Enterprising2",
        "label": "Manage a retail store",
        "type": "radio",
        "choices": [
            {"name": "Strongly Dislike", "value":1},
            {"name": "DisLike", "value":2},
            {"name": "Unsure", "value":3},
            {"name": "Like", "value":4},
            {"name": "Strongly Like", "value":5}
        ]
    },
    {
        "name": "Conventional1",
        "label": "Develop a spreadsheet using computer software",
        "type": "radio",
        "choices": [
            {"name": "Strongly Dislike", "value":1},
            {"name": "DisLike", "value":2},
            {"name": "Unsure", "value":3},
            {"name": "Like", "value":4},
            {"name": "Strongly Like", "value":5}
        ]
    },
    {
        "name": "Conventional2",
        "label": "Proofread records or forms",
        "type": "radio",
        "choices": [
            {"name": "Strongly Dislike", "value":1},
            {"name": "DisLike", "value":2},
            {"name": "Unsure", "value":3},
            {"name": "Like", "value":4},
            {"name": "Strongly Like", "value":5}
        ]
    }
]

"""


@login_required(login_url='login')
def test(request):
    global a

    form_class = get_form(a)
    data = {}
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            r = 0
            i = 0
            a = 0
            s = 0
            e = 0
            c = 0

            if form.is_valid():

                # r = int(form.cleaned_data['Realistic1']) + int(form.cleaned_data['Realistic2']) + int(form.cleaned_data['Realistic3']) + int(form.cleaned_data['Realistic4']) + int(form.cleaned_data['Realistic5']) + int(form.cleaned_data['Realistic6']) + int(form.cleaned_data['Realistic7']) + int(form.cleaned_data['Realistic8']) + int(form.cleaned_data['Realistic9']) + int(form.cleaned_data['Realistic10'])

                # i = int(form.cleaned_data['Investigative1']) + int(form.cleaned_data['Investigative2']) + int(form.cleaned_data['Investigative3'])+ int(form.cleaned_data['Investigative4']) + int(form.cleaned_data['Investigative5']) + int(form.cleaned_data['Investigative6']) + int(form.cleaned_data['Investigative10'])

                # a = int(form.cleaned_data['Artistic1']) + int(form.cleaned_data['Artistic2']) + int(form.cleaned_data['Artistic3'])+ int(form.cleaned_data['Artistic4']) + int(form.cleaned_data['Artistic5']) + int(form.cleaned_data['Artistic6']) + int(form.cleaned_data['Artistic7']) + int(form.cleaned_data['Artistic8']) + int(form.cleaned_data['Artistic9']) + int(form.cleaned_data['Artistic10'])

                # s = int(form.cleaned_data['Social1']) + int(form.cleaned_data['Social2']) + int(form.cleaned_data['Social3'])+ int(form.cleaned_data['Social4']) + int(form.cleaned_data['Social5']) + int(form.cleaned_data['Social6']) +int(form.cleaned_data['Social7']) + int(form.cleaned_data['Social8']) + int(form.cleaned_data['Social9']) +int(form.cleaned_data['Social10'])

                # e = int(form.cleaned_data['Enterprising1']) + int(form.cleaned_data['Enterprising2']) + int(form.cleaned_data['Enterprising3'])+ int(form.cleaned_data['Enterprising4']) + int(form.cleaned_data['Enterprising5']) + int(form.cleaned_data['Enterprising6']) + int(form.cleaned_data['Enterprising7']) + int(form.cleaned_data['Enterprising8']) + int(form.cleaned_data['Enterprising9']) + int(form.cleaned_data['Enterprising10'])

                # c = int(form.cleaned_data['Conventional1']) + int(form.cleaned_data['Conventional2']) + int(form.cleaned_data['Conventional3'])+ int(form.cleaned_data['Conventional4']) + int(form.cleaned_data['Conventional5']) + int(form.cleaned_data['Conventional6']) + int(form.cleaned_data['Conventional7']) + int(form.cleaned_data['Conventional8']) + int(form.cleaned_data['Conventional9']) + int(form.cleaned_data['Conventional10'])

                r = int(form.cleaned_data['Realistic1']) + \
                    int(form.cleaned_data['Realistic2'])
                i = int(form.cleaned_data['Investigative1']) + \
                    int(form.cleaned_data['Investigative2'])
                a = int(form.cleaned_data['Artistic1']) + \
                    int(form.cleaned_data['Artistic2'])
                s = int(form.cleaned_data['Social1']) + \
                    int(form.cleaned_data['Social2'])
                e = int(form.cleaned_data['Enterprising1']) + \
                    int(form.cleaned_data['Enterprising2'])
                c = int(form.cleaned_data['Conventional1']) + \
                    int(form.cleaned_data['Conventional2'])
                user = User.objects.get(username=request.user.get_username())

                try:

                    person = student.objects.get(Identification_no=user)
                    user_pers, created = User_Personality.objects.update_or_create(user_id=person, defaults={
                                                                                   'Realistic': r/5, 'Investigative': i/5, 'Artistic': a/5, 'Social': s/5, 'Enterprising': e/5, 'Conventional': c/5, })
                    print(user_pers)

                    # user_pers.Realistic = r/5
                    # user_pers.Investigative = i/5
                    # user_pers.Artistic = a/5
                    # user_pers.Social = s/5
                    # user_pers.Enterprising = e/5
                    # user_pers.Conventional = c/5

                    # user_pers.save()
                    return redirect('result')

                except:
                    return render(request, 'personality/test.html')

        return redirect('personality/test')

    else:
        form = form_class()

    context = {'form': form,  'data': data,
               'profile_test': 'active', 'crumb': 'Profile Test', }

    return render(request, "personality/test.html", context)


@login_required(login_url='login')
def result(request):
    u = User.objects.get(username=request.user.get_username())
    person = student.objects.get(Identification_no=u)
    message = ''
    results = None
    record = []

    if User_Personality.objects.filter(user_id=person):
        results = list(User_Personality.objects.filter(
            user_id=person).values())
        record.append(results[0]['Realistic'])
        record.append(results[0]['Investigative'])
        record.append(results[0]['Artistic'])
        record.append(results[0]['Social'])
        record.append(results[0]['Enterprising'])
        record.append(results[0]['Conventional'])

    else:
        return redirect('personality/test')

    context = {'student': student,
               'results': record,
               'message': message,
               'profile_test': 'active',
               'Realistic': record[0]*5,
               'Investigative':record[1]*5,
               'Artistic':record[2]*5,
               'Social': record[3]*5,
               'Enterprising':record[4]*5,
               'Conventional': record[5]*5,
               
               'crumb': 'Profile Test'}
    print(results, record, "uu")

    return render(request, 'personality/result.html', context)


def take(request):
    try:
        # child_user = Child.objects.get(user=request.user)

        quiz_words = Questions.objects.all()
        area_list = []

        wordList = []
        for items in quiz_words:
            wordList.append(str(items))

        for items in quiz_words:

            area_list.append(str(items.area))


        context = {
            # 'newuser': child_user,
            'word': quiz_words,
            'data': wordList,
            'area': area_list,
            # 'wordlimit': wordlimit,
        }
        return render(request, 'personality/take.html', context)
    except:
  
        return render(request, 'personality/take.html', {})

def save(request):
    if request.method == 'POST':
        u = User.objects.get(username=request.user.get_username())
        person = student.objects.get(Identification_no=u)
        Realistic = float(request.POST.get('Realistic'))
        Investigative = float(request.POST.get('Investigative'))
        Artistic = float(request.POST.get('Artistic'))
        Social = float(request.POST.get('Social'))
        Enterprising = float(request.POST.get('Enterprising'))
        Conventional = float(request.POST.get('Conventional'))

        result_url = reverse('personality:result')

        
        print(result_url)
        print()


        print(person)
        try:

            # person = student.objects.get(Identification_no=person)
            print(person)
            user_pers, created = User_Personality.objects.update_or_create(user_id=person, defaults={
                                                                           'Realistic': Realistic/5, 'Investigative': Investigative/5, 'Artistic': Artistic/5, 'Social': Social/5, 'Enterprising': Enterprising/5, 'Conventional': Conventional/5, })
            print('hello', user_pers)

            
            return JsonResponse(status=302, data={"url": request.build_absolute_uri(result_url)})

            # return redirect('personalitytest:test')
            # return JsonResponse({'status': 'success'})

        except :
            # print(e)
            print('bye', user_pers)
            print(request)
            return render(request, 'personality/test.html')
    return render(request, 'personality/test.html')

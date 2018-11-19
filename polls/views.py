from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from polls.models import Question


def index(request):
    question = Question.objects.all()

    return render(request, 'polls/index.html',
                  {'question' : question})
    #return HttpResponse("polls index")


def detail(request, question_id):
    q = Question.objects.get(id=question_id) # 조건에 맞는 데이터 1개 조회
    c = q.choice_set.all()
    #choice = ''
    #for a in c:
    #    choice = choice + a.choice_text + '\t'
    return render(request, 'polls/detail.html', \
                  {'question' : q.question_text,
                   'num':q.id, 'choice' : c })
    #             request  템플릿  컨텍스트(데이터/모델) >> 딕셔너리 형태
    #return HttpResponse(q.question_text + '<br>' + choice)

def detail2(request, num1, num2):
    return HttpResponse(num1 + num2)

def results(request, question_id):
    response = "You're looking at results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id): # 투표 페이지

    try:
        select = request.POST['select']

        q = Question.objects.get(id = question_id)
        c = q.choice_set.get(id=select)
        c.votes += 1
        c.save()

        print(select)

    except:
        pass

    return render(
        request,
        'polls/result.html',
        {'q':q}
    )


    return HttpResponse("ok")


def save(request, question_id):
    q = request.POST['q']
    question = Question.objects.get(id=question_id)
    question.question_text = q
    question.save()
    return HttpResponse("수정 완료")

def edit(request, question_id):
    q = Question.objects.get(id = question_id)

    return render(
        request, 'polls/edit.html', {'q':q}
    )
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('calculator/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }

    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'calculator/detail.html', {'question': question})

def results(request, question_id):
    response = "Results of question %s"
    return HttpResponse(response % question_id)

def calculate(request):
    try: 
        v = float(request.POST.get('4'))
        u = float(request.POST.get('3'))
        p = float(request.POST.get('2'))
    except TypeError:
        return HttpResponse("You have to fill out all of the assessment! <a href='../'>Go back!</a>")

    result = (1-p) * u * (1-v)
    return render(request, 'calculator/result.html', {'result' : result})



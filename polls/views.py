from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from  django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    content_jbject_name = 'lasted_question_list'

    def get_queryset(self):
        """
        :return: last 2 published questions
        """
        return Question.objects.filter(pub_date__lte=timezone.now())\
            .order_by('-pub_date')[:2]


class DetailView(generic.DetailView):

    # по какой модели действовать
    model = Question
    templaet_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class Resultview(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def index(request):

    """
        Этот код загружает вызываемый шаблон polls/index.htmlи
        передает ему контекст. Контекст - это словарь, сопоставляющий
        имена переменных шаблона с объектами Python.
    """

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
   # try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
   #     raise Http404("Question does not exist")

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

    #return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    #response = "you're looking at the result of question %s"
    #return HttpResponse(response % question_id)

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST['choice'] ->
        # позволяет вам получать доступ к отправленным данным по имени ключа.
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    # код проверяет KeyError и повторно отображает форму вопроса с сообщением
    # об ошибке, если choiceоно не указано.
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_maeesage': "You didn't select a choice",
        })
    else:
        selected_choice.votes+=1
        selected_choice.save()

        # URL-адрес, на который будет перенаправлен пользователь.
        # Как указано в комментарии Python выше, вы всегда должны возвращать
        # HttpResponseRedirect после успешной обработки данных POST.

        # reverse ->  этот reverse()вызов вернет строку вида '/polls/3/results/'
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
from django.urls import path
from django.conf.urls import url
from . import views

"""
        Он находит указанную переменную urlpatterns и просматривает шаблоны по порядку. 
        После нахождения совпадения в 'polls/', он удаляет совпадающий текст 
        ( 'polls/') и отправляет оставшийся текст - '34/'- в URLconf 'polls.urls' для 
        дальнейшей обработки. Там он совпадает '<int:question_id>/'

        detail(request=<HttpRequest object>, question_id=34)
"""

"""
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/result/', views.result, name='result'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
"""

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

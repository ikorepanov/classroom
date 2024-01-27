from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     template = 'seats/index.html'
#     title = 'Главная страница'
#     text = 'Главная страница'
#     context = {
#         'title': title,
#         'text': text,
#     }

#     return render(request, template, context)

def index(request):
    return HttpResponse(
        'Ты <i>не можешь</i> получить правильные <b>ответы</b>,<br> '
        'если у тебя нет правильных <s>вопросов</s> запросов.'
    )

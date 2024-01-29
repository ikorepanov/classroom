from django.shortcuts import render


def index(request):
    template = 'seats/index.html'
    title = 'Главная страница'
    text = 'Главная страница'
    some = 'Some'
    context = {
        'title': title,
        'text': text,
        'some': some,
    }

    return render(request, template, context)

def test(request):
    template = 'seats/test.html'
    title = 'Тестовая страница'
    text = 'Тестовая страница'
    some = 'Some Test'
    context = {
        'title': title,
        'text': text,
        'some': some,
    }

    return render(request, template, context)

from django.shortcuts import render
# from .forms import ArrangementForm, SomeForm


def index(request):
    template = 'seats/index.html'
    title = 'Главная страница'
    text = 'Главная страница'
    some = 'Main'
    context = {
        'title': title,
        'text': text,
        'some': some,
    }
    return render(request, template, context)

    # template = 'seats/index.html'
    # title = 'Главная страница'
    # text = 'Главная страница'
    # some = 'Card Subtitle'

    # if request.method == 'POST':
    #     arrangementform = ArrangementForm(request.POST)
    #     someform = SomeForm(request.POST)
    #     if arrangementform.is_valid():
    #         columns = arrangementform.cleaned_data['columns']
    #         rows = arrangementform.cleaned_data['rows']
    #         print('\n')
    #         print('Columns, rows: ', columns, rows)
    #         arrangementform.save()
    #     return render(request, template, {'arrangementform': arrangementform})

    # else:
    #     arrangementform = ArrangementForm()
    #     someform = SomeForm()

    # context = {
    #     'title': title,
    #     'text': text,
    #     'some': some,
    #     'arrangementform': arrangementform,
    #     'someform': someform,
    # }
    # print('КОНТЕКСТ: ', context)
    # return render(request, template, context)


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


def success(request):
    template = 'seats/success.html'
    title = 'Страница успеха'
    text = 'Страница успеха'
    some = 'Sucess'
    context = {
        'title': title,
        'text': text,
        'some': some,
    }
    return render(request, template, context)

from django.shortcuts import redirect, render
from .forms import SeatsForm
from .utils import main


def index(request):
    template = 'seats/index.html'
    title = 'Главная страница'
    text = 'Главная страница'
    some = 'Some'
    seats = None

    if request.method == 'POST':
        form = SeatsForm(request.POST)
        if form.is_valid():
            variants = form.cleaned_data['variants']
            rows = form.cleaned_data['rows']
            desks = form.cleaned_data['desks']
            pupils_lst = form.cleaned_data['pupils_lst'].split()
            print(variants, rows, desks, pupils_lst)
            columns = variants * rows
            print(columns)
            seats = dict(main(desks, columns, pupils_lst))  # NB! Операцию произвести в utils.py
            print('РАССАДКА: ', seats)

    else:
        form = SeatsForm()

    context = {
        'title': title,
        'text': text,
        'some': some,
        'form': form,
        'seats': seats
    }
    print('КОНТЕКСТ: ', context)
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

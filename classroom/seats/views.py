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
            seats = dict(sorted(seats.items(), reverse=True))
            for key, value in seats.items():
                value = value.reverse()
            list_of_lists = list(seats.values())
            transposed_list = list(map(list, zip(*list_of_lists)))
            print('РАССАДКА: ', seats)

    else:
        form = SeatsForm()

    context = {
        'title': title,
        'text': text,
        'some': some,
        'form': form,
        'seats': seats,
        'transposed_list': transposed_list,
        # 'rows': rows,
        'variants': variants,
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

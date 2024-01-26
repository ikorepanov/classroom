import random
from collections import defaultdict

pupils_lst = ['Alisa', 'Filipp', 'Katya', 'Polina', 'Vadim']
# pupils_lst = ['Alisa']


# variants = int(input('Enter number of variants: \n'))
# rows = int(input('Enter number of rows: \n'))
# desks = int(input('Enter number of rows of desks: \n'))

# columns = variants * rows

columns = 2
desks = 3


class Pupil:
    def __init__(self, name):
        self.name = name


class Seat:
    def __init__(self, column, desk, pupil):
        self.column = column
        self.desk = desk
        self.pupil = pupil


seats = defaultdict(list)

for i in range(columns):
    for j in range(desks):
        seats[i].append(Seat(i, j, None))

print('МЕСТА: ', seats)

for i in range(columns):
    for seat in seats[i]:
        print('***: ', seat.column, seat.desk)

pupils = [Pupil(pupil) for pupil in pupils_lst]

print('УЧЕНИКИ: ', pupils)

shuffled_pupils = random.sample(pupils, k=len(pupils))
print('ПЕРЕПУТАННЫЕ УЧЕНИКИ: ', shuffled_pupils)

k = desks
print('КОЛИЧЕСТВО РЯДОВ ПАРТ В КЛАССЕ: ', k)
seats_with_pupils = defaultdict(list)

while k > 0:
    keys = random.sample(list(seats), columns)
    print('ПЕРЕМЕШАННЫЕ КЛЮЧИ: ', keys)
    for i in range(columns):
        value = seats[keys[i]]
        print(f'ЗНАЧЕНИЕ КЛЮЧА {i}: ', value)
        seat = value.pop(random.randint(0, len(value)-1))
        print('ИЗВЛЕЧЕННОЕ МЕСТО: ', seat)
        try:
            setattr(seat, 'pupil', shuffled_pupils.pop(0))
        except IndexError:
            print('УЧЕНИЧКИ ЗАКОНЧИЛИСЬ :-)')
        column_row = getattr(seat, 'column')
        desk_row = getattr(seat, 'desk')
        # seats_with_pupils[column_row].insert(desk_row, seat)
        seats_with_pupils[column_row].append(seat)
        print(column_row, desk_row)

    k -= 1

for i in range(columns):
    for seat in seats_with_pupils[i]:
        print('&&&: ', seat.column, seat.desk)

for i in range(columns):
    seats_with_pupils[i].sort(key=lambda seat: seat.desk)
    # sorted(seats_with_pupils[i], key=lambda seat: seat.desk)

for i in range(columns):
    for seat in seats_with_pupils[i]:
        print('###: ', seat.column, seat.desk)

print('СМОТРИ СЮДА: СЛОВАРЬ С УСАЖЕННЫМИ УЧЕНИКАМИ: ', seats_with_pupils)
for i in range(columns):
    print(seats_with_pupils[i])
    for j in range(len(seats_with_pupils[i])):
        try:
            print(seats_with_pupils[i][j].pupil.name)
        except AttributeError:
            print('Это место осталось свободным')

print('МЕСТА: ', seats_with_pupils)

# for seat in seats_with_pupils[0]:
#     print('###: ', seat.column, seat.desk)

for i in range(columns):
    ryad_s_kotorim_rabotaem = seats_with_pupils[i]
    print(ryad_s_kotorim_rabotaem)
    count = 0
    for index, seat in reversed(list(enumerate(ryad_s_kotorim_rabotaem))):
        if seat.pupil is not None:
            count += 1
            print('Раз!')
        else:
            if count == 0:
                print('Два!')
                continue
            else:
                print('Три!')
                for j in range(index, index+count):
                    seat = ryad_s_kotorim_rabotaem[j]
                    print('ВАЖНО!', seat)
                    print('Четыре!')
                    next_seat = ryad_s_kotorim_rabotaem[j+1]
                    print('Следующее: ', next_seat)
                    print('Индекс места, с которым работаем: ', j)
                    print('Индекс следующего места: ', j+1)
                    searched_pupil = next_seat.pupil
                    print('Найденный ученик: ', searched_pupil)
                    setattr(next_seat, 'pupil', None)
                    setattr(seat, 'pupil', searched_pupil)
                    print('ПЕРЕСАДИЛИ!')
    print(count)

print('СМОТРИ СЮДА: СЛОВАРЬ С пересаженными УЧЕНИКАМИ: ', seats_with_pupils)
for i in range(columns):
    print(seats_with_pupils[i])
    for j in range(len(seats_with_pupils[i])):
        try:
            print(seats_with_pupils[i][j].pupil.name)
        except AttributeError:
            print('Это место осталось свободным')

print(seats_with_pupils)

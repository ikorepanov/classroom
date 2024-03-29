import random
from collections import defaultdict


class Pupil:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Seat:
    def __init__(self, column, desk):
        self.column = column
        self.desk = desk
        self.pupil = None

    def __str__(self):
        return f"Seat - Desk: {self.desk}, Column: {self.column}, Pupil: {self.pupil}"


class Classroom:
    def __init__(self, columns, desks):
        self.columns = columns
        self.desks = desks
        self.seats = self.create_seats()

    def create_seats(self):
        seats = defaultdict(list)
        for i in range(self.columns):
            for j in range(self.desks):
                seats[i].append(Seat(i, j))
        return seats

# # 1. Перемешиваем всё каждый раз
#     def assign_pupils_to_seats(self, pupils):
#         shuffled_pupils = random.sample(pupils, k=len(pupils))
#         seats_with_pupils = defaultdict(list)
#         remaining_desks = self.desks

#         while remaining_desks > 0:
#             keys = random.sample(list(self.seats), self.columns)  # NB!
#             for i in range(self.columns):
#                 value = self.seats[keys[i]]
#                 seat = value.pop(random.randint(0, len(value)-1))  # NB!
#                 try:
#                     setattr(seat, 'pupil', shuffled_pupils.pop(0))
#                 except IndexError:
#                     print('No more pupils available.')
#                 seats_with_pupils[seat.column].append(seat)
#             remaining_desks -= 1
#         return seats_with_pupils

# # 2. Перемешиваем всё (учеников, ключи) - один раз
    # def assign_pupils_to_seats(self, pupils):
    #     shuffled_pupils = random.sample(pupils, k=len(pupils))
    #     seats_with_pupils = defaultdict(list)
    #     keys = random.sample(list(self.seats), self.columns)
    #     remaining_desks = self.desks
    #     while remaining_desks > 0:
    #         for key in keys:
    #             seat = self.seats[key][-remaining_desks]
    #             try:
    #                 setattr(seat, 'pupil', shuffled_pupils.pop())
    #             except IndexError:
    #                 print('No more pupils available.')
    #             seats_with_pupils[key].append(seat)
    #         remaining_desks -= 1
    #     return seats_with_pupils

# 3. Перемешиваем только учеников
    def assign_pupils_to_seats(self, pupils):
        shuffled_pupils = random.sample(pupils, k=len(pupils))
        seats_with_pupils = defaultdict(list)

        keys = range(self.columns)
        remaining_desks = self.desks
        while remaining_desks > 0:
            for key in keys:
                seat = self.seats[key][-remaining_desks]
                try:
                    setattr(seat, 'pupil', shuffled_pupils.pop())
                except IndexError:
                    print('No more pupils available.')
                seats_with_pupils[key].append(seat)
            remaining_desks -= 1
        return seats_with_pupils

# # 4. Перемешиваем учеников один раз, ставим на произвольные места в колонке (а не по порядку). Колонки идут по порядку
#     def assign_pupils_to_seats(self, pupils):
#         shuffled_pupils = random.sample(pupils, k=len(pupils))
#         shuffled_pupils = random.choices(pupils, k=len(pupils))
#         seats_with_pupils = defaultdict(list)

#         keys = range(self.columns)
#         remaining_desks = self.desks
#         while remaining_desks > 0:
#             for key in keys:
#                 value = self.seats[key]
#                 seat = value.pop(random.randint(0, len(value)-1))
#                 try:
#                     setattr(seat, 'pupil', shuffled_pupils.pop())
#                 except IndexError:
#                     print('No more pupils available.')
#                 seats_with_pupils[key].append(seat)
#             remaining_desks -= 1
#         return seats_with_pupils

# # 5. Перемешиваем всё, кроме учеников
#     def assign_pupils_to_seats(self, pupils):
#         shuffled_pupils = pupils
#         seats_with_pupils = defaultdict(list)
#         remaining_desks = self.desks

#         while remaining_desks > 0:
#             keys = random.sample(list(self.seats), self.columns)  # NB!
#             for i in range(self.columns):
#                 value = self.seats[keys[i]]
#                 seat = value.pop(random.randint(0, len(value)-1))  # NB!
#                 try:
#                     setattr(seat, 'pupil', shuffled_pupils.pop(0))
#                 except IndexError:
#                     print('No more pupils available.')
#                 seats_with_pupils[seat.column].append(seat)
#             remaining_desks -= 1
#         return seats_with_pupils

    def sort_seats(self):
        for i in range(self.columns):
            self.seats[i].sort(key=lambda seat: seat.desk)

    def rearrange_seats(self):
        for i in range(self.columns):
            var = self.seats[i]
            count = 0
            for index, seat in reversed(list(enumerate(var))):
                if seat.pupil is not None:
                    count += 1
                else:
                    if count == 0:
                        continue
                    else:
                        for j in range(index, index+count):
                            seat = var[j]
                            next_seat = var[j+1]
                            searched_pupil = next_seat.pupil
                            setattr(next_seat, 'pupil', None)
                            setattr(seat, 'pupil', searched_pupil)

    def check_order_of_seats_append(self):
        for i in range(self.columns):
            for seat in self.seats[i]:
                print('***: ', seat.column, seat.desk)

    def check_free_seats(self):
        for i in range(self.columns):
            print(self.seats[i])
            for j in range(len(self.seats[i])):
                try:
                    print(self.seats[i][j].pupil.name)
                except AttributeError:
                    print('Это место осталось свободным')


# def main():
def main(desks, columns, pupils_lst):
    # pupils_lst = ['Alisa', 'Filipp', 'Katya', 'Polina', 'Vadim']

    # pupils_lst = ['Alisa']
    # variants = int(input('Enter number of variants: \n'))
    # rows = int(input('Enter number of rows: \n'))
    # desks = int(input('Enter number of rows of desks: \n'))

    # variants = 2
    # rows = 1
    # desks = 3
    # columns = variants * rows

    pupils = [Pupil(pupil) for pupil in pupils_lst]

    klass = Classroom(columns, desks)

    print('МЕСТА: ', klass.seats)

    klass.check_order_of_seats_append()

    print('УЧЕНИКИ: ', pupils)

    klass.seats = klass.assign_pupils_to_seats(pupils)

    klass.check_order_of_seats_append()

    klass.sort_seats()

    klass.check_order_of_seats_append()

    klass.check_free_seats()

    klass.rearrange_seats()

    klass.check_free_seats()

    return klass.seats


if __name__ == '__main__':
    main()

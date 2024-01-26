#  Первая версия кода

import random

pupils = ['Alisa', 'Filipp', 'Katya', 'Polina', 'Vadim']

seats = {
    'first': [1, 2, 3],
    'second': [4, 5, 6]
}

k = len(seats['first'])
# print(k)
order_lst = []
while k > 0:
    keys = random.sample(list(seats), len(seats))
    # print(keys)
    for i in range(len(keys)):
        value = seats[keys[i]]
        # print(value)
        seat = value.pop(random.randint(0, len(value)-1))
        order_lst.append(str(seat))
        # print(seat)
        # print(value)
        seats[keys[i]] = value
    k -= 1
# print(seats)
print(order_lst)
shuffled_pupils = random.sample(pupils, k=len(pupils))
print(shuffled_pupils)

z = [' '.join(item) for item in zip(order_lst, shuffled_pupils)]
print(z)

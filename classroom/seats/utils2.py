import numpy as np

number_of_linear_arrays = 6

indices = np.arange(number_of_linear_arrays)

mentiones_indices = []
count = 0
number_of_seating_arrangements = 9
last_index = None

while True:
    print('Цикл начинается здесь')
    for i in range(len(indices)):
        if count == number_of_seating_arrangements:
            break
        probabilities = [1 / (len(indices)-i) for j in range(len(indices))]
        for index in mentiones_indices:
            probabilities[index] = 0
        array_probs = np.array(probabilities)
        index = np.random.choice(indices, p=array_probs)
        if index == last_index and count % number_of_linear_arrays == 0:
            print('Прерывание!', index)
            break
        mentiones_indices.append(index)
        count += 1
        print('РЕЗУЛЬТАТ: ', index)
        # print('Количество операций генерации индекса: ', count)
    last_index = index
    mentiones_indices.clear()
    if count == number_of_seating_arrangements:
        break

import numpy as np

axis = 6

arr = np.arange(axis)

used_indices = []
count = 0
number_of_arrangements = 9
last_index = None

while True:
    print('Цикл начинается здесь')
    for i in range(len(arr)):
        if count == number_of_arrangements:
            break
        probabilities = [1 / (len(arr)-i) for j in range(len(arr))]
        for index in used_indices:
            probabilities[index] = 0
        array_probs = np.array(probabilities)
        index = np.random.choice(arr, p=array_probs)
        if index == last_index and count % axis == 0:
            print('Прерывание!', index)
            break
        used_indices.append(index)
        count += 1
        print('РЕЗУЛЬТАТ: ', index)
        # print('Количество операций генерации индекса: ', count)
    last_index = index
    used_indices.clear()
    if count == number_of_arrangements:
        break

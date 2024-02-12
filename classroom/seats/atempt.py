import numpy as np


def generate_seating_order(number_of_linear_arrays,
                           number_of_seating_arrangements):

    indices = np.arange(number_of_linear_arrays)
    mentioned_indices = []
    count = 0
    last_index = None
    seating_order = []

    while True:
        for i in range(len(indices)):
            if count == number_of_seating_arrangements:
                break
            probabilities = [1 / (len(indices)-i) for j in range(len(indices))]
            for index in mentioned_indices:
                probabilities[index] = 0
            array_probs = np.array(probabilities)
            index = np.random.choice(indices, p=array_probs)
            if index == last_index and count % number_of_linear_arrays == 0:
                break
            mentioned_indices.append(index)
            count += 1
            seating_order.append(index)
        last_index = index
        mentioned_indices.clear()
        if count == number_of_seating_arrangements:
            break
    return seating_order


number_of_linear_arrays = 6
number_of_seating_arrangements = 9

print(generate_seating_order(number_of_linear_arrays,
                             number_of_seating_arrangements))

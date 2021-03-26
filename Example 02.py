array = [1, 10, 5, 6, -1]
length = len(array)

for i in range(length):

    min_number = 10000
    min_number_index = 10000
    for m in range(i, length):
        if array[m] < min_number:
            min_number = array[m]
            min_number_index = m

    temp = array[i]
    array[i] = array[min_number_index]
    array[min_number_index] = temp

print(array)
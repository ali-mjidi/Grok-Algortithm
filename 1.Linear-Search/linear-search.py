def linear_search(array, item):
    for index in range(len(array)):
        if (array[index] == item):
            return index

    return None


my_array = [i for i in range(1, 101)]
print(linear_search(my_array, 99))

wakeup_times = [16, 49, 3, 12, 56, 49, 55, 22, 13, 46, 19, 55, 46, 13, 25, 56, 9, 48, 45]


def bubble_sort_1(l):
    # TODO: Implement bubble sort solution
    array = l
    indexing_length = len(array) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if array[i] > array[i + 1]:
                sorted = False
                array[i], array[i+1] = array[i+1], array[i]

    return array


print(bubble_sort_1(wakeup_times))
print("Pass" if (wakeup_times[0] == 3) else "Fail")

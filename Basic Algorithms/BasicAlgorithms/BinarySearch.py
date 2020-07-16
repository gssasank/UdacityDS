def binary_search(array, target):
    first_element = 0
    last_element = len(array) - 1
    while first_element <= last_element:
        key = (first_element+last_element)//2
        if array[key] == target:
            return key
        else:
            if target > array[key]:
                first_element = key
            elif target < array[key]:
                last_element = key


def test_function(test):
    answer = binary_search(test[0], test[1])
    if answer == test[2]:
        print("Pass! ☕️")
    else:
        print("Fail!")


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
index = 6
test_case = [array, target, index]
test_function(test_case)
print("great")

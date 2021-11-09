A = [0, 1, 2, 3, 5, 6]
left = 0
right = len(A)-1

def input_list_numbers():
    pass

def fun(numbers, left, right, key):
    if (right - left) == 0:
        if numbers[left] == key:
            return left
        return None

    midle = (right + left) // 2
    if numbers[midle] == key:
        return midle
    if numbers[midle] < key:
        return fun(numbers, midle+1, right, key)
    else:
        return fun(numbers, left, midle-1, key)


def print_result(A, index):
    if index is None:
        print("Числа нет")
    else:
        print(index, A[index])


def main():
    index = fun(A, left, right, key = 4)
    print_result(A, index)

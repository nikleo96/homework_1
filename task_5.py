import random

def random_shift(list_num, len_list):
    x, y = random.randint(0, len_list-1), random.randint(0, len_list-1)
    list_num[x], list_num[y] = list_num[y], list_num[x]
    return list_num


def check_finish(list_num, list_num_check):
    if list_num == list_num_check:
        return True
    return False


def main():
    list_numbers = [5,6,3,6,4,8,9,4,0,1,2]
    list_numbers_check = sorted(list_numbers)
    len_list = len(list_numbers)

    count_iteration = 0
    while not check_finish(list_numbers, list_numbers_check):
        list_numbers = random_shift(list_numbers, len_list)
        count_iteration += 1
    print("Кол-во итераций: ", count_iteration, ". Отсортированный список: ", *list_numbers)

main()
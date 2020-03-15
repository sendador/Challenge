from itertools import groupby


def check_adjacent(number_list):

    adjacent_groups = [len(list(g)) for k, g in groupby(number_list)]
    identical_adjacent_digits_counter = len(
        list(u for u in adjacent_groups if u > 1))

    return identical_adjacent_digits_counter


def check_increasing_numbers(number_list):

    return all(x <= y for x, y in zip(number_list, number_list[1:]))


def numbers_range(start_number, end_number):
    numbers_list = []
    for x in range(start_number, end_number+1):
        numbers_list.append(str(x))
    return numbers_list


def list_of_possible_combinations(number_list):
    specific_list = []
    result_list = []
    for numbers in number_list:
        if (check_adjacent(specific_list) > 1) and (check_increasing_numbers(specific_list) == True):
            result_list.append(int(numbers)-1)
        specific_list = []
        for number in numbers:
            specific_list.append(int(number))
    return result_list


number_list = numbers_range(372**2, 809**2)
answer = list_of_possible_combinations(number_list)
print(f"You have to check {len(answer)} numbers. That's a bummer bro")

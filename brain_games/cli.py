import prompt
import random


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def start_game(func, text, count_game):
    back_func = func(text)
    if count_game == 0 and is_true(back_func):
        print(f'Congratulations, {text}!')
        return
    elif is_true(back_func):
        return start_game(func, text, count_game - 1)
    else:
        return


def is_true(text):
    return True if text else False


def is_answer(first_answer, second_answer):
    return True if first_answer == second_answer else False


def is_even(num, divider=2):
    return True if num % divider == 0 else False


def correct_answer(num=2):
    return 'yes' if is_even(num) else 'no'


def is_prime(value):
    list_pride = [2, 3, 5, 7]
    if value in list_pride:
        return 'yes'
    else:
        first_divider = 2
        last_divider = 10
        list_pride = [num for num in range(first_divider, last_divider)
                        \
                      if is_even(value, num)]
        return 'yes' if len(list_pride) < 1 else 'no'


def get_progression():
    random_progressive_size = random.randint(5, 10)
    random_application = random.randint(1, 5)
    first_meaning = random.randint(0, 20)
    list_progression = []
    acc = first_meaning

    for item in range(0, random_progressive_size):
        acc += random_application
        list_progression.append(acc)

    return list_progression


def change_value(arr, value, index):
    changed_value = 0
    new_arr = []
    for num in range(0, len(arr)):
        if index == num:
            changed_value = arr[index]
            new_arr.append(value)
            continue
        new_arr.append(arr[num])

    return new_arr, changed_value


def arr_to_string(arr):
    string = ''
    for value in range(0, len(arr)):
        string += f'{arr[value]} '
    return string

from random import randint
import prompt


def is_even(num):
    return True if num % 2 == 0 else False


def correct_answer(num):
    return 'yes' if is_even(num) else 'no'


def is_answer(first_answer, second_answer):
    return True if first_answer == second_answer else False


def even(name):
    random_number = randint(1, 100)
    print(f'Question: {random_number}')
    user_answer = prompt.string('Your answer: ')

    true_answer = correct_answer(random_number)

    check_answer = is_answer(user_answer, true_answer)

    if check_answer:
        print('Correct!')
        return True

    else:
        print(f"'{user_answer}' is wrong answer ;(."
              f"Correct answer was '{true_answer} '")
        print(f"Let's try again, {name}!")
        return False

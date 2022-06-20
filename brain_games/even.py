from random import randint
from .cli import correct_answer, is_answer, start_game, welcome_user
import prompt


def start_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    start_game(even, name, 2)


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

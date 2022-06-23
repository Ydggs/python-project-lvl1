import prompt
from .cli import welcome_user, start_game, is_answer
import random


def start_calc():
    name = welcome_user()
    print('What is the result of the expression?')
    start_game(calc, name, 2)


def calc(name):
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    random_symbols = random.choice(['+', '*', '-'])
    true_answer = eval(
        f'{first_number}{random_symbols}{second_number}')

    print(f'Question: {first_number} {random_symbols} {second_number}')

    user_answer = prompt.real('You answer: ')

    if is_answer(true_answer, user_answer):
        print('Correct!')
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(."
              f"Correct answer was '{true_answer} '")
        print(f"Let's try again, {name}!")
        return False

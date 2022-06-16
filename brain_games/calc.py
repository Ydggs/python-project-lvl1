import prompt
from .cli import welcome_user
import random


def calc():

    name = welcome_user()
    index = 0

    print('What is the result of the expression?')

    while index < 3:
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        random_symbols = random.choice(['+', '/', '*', '-'])
        numbers_sum = round(eval(
            f'{first_number}{random_symbols}{second_number}'), 1)

        print(f'Question: {first_number} {random_symbols} {second_number}')

        user_answer = prompt.real('You answer: ')
        if numbers_sum == user_answer:
            print('Correct!')
            index += 1
            continue

        return print(f"'{user_answer}' is wrong answer ;(."
                     f"Correct answer was '{numbers_sum}'"
                     f"\nLet's try again, {name}")

    return print(f'Congratulations, {name}!')


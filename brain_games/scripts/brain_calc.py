import prompt
from ..cli import welcome_user
import random


def main():
    name = welcome_user()
    index = 0

    print('What is the result of the expression?')

    while index != 3:
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        random_symbols = random.choice(['+', '/', '*', '-'])
        print(f'Question: {first_number} {random_symbols} {second_number}')
        numbers_sum = eval(f'{first_number}{random_symbols}{second_number}')
        answer_user = prompt.integer('You answer: ')
        if numbers_sum == answer_user:
            print('Correct!')
            index += 1
            continue
        print(f"'{answer_user}' is wrong answer ;(."
              f"Correct answer was '{numbers_sum}'"
              f"Let's try again, {name}")
        break

    if index == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

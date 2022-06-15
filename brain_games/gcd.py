from .cli import welcome_user
import prompt
import random


def gcd():
    name = welcome_user()
    index = 0

    print('Find the greatest common divisor of given numbers.')

    while index <= 3:
        first_num = random.randint(0, 100)
        second_num = random.randint(0, 100)
        greatest_num = max(first_num, second_num)

        print(f'Question: {first_num} {second_num}')
        answer_user = int(prompt.integer('You answer: '))

        for num in range(greatest_num, 0, -1):
            if (first_num % num == 0) and (second_num % num == 0)\
                    and (num == answer_user):
                index += 1
                print('Correct!')
                break
            elif (first_num % num == 0) and (second_num % num == 0)\
                    and (num != answer_user):
                return print(f"'{answer_user}' is wrong answer ;(."
                             f"Correct answer was '{num} '"
                             f"Let's try again, {name}")

    if index == 3:
        print(f'Congratulations, {name}!')

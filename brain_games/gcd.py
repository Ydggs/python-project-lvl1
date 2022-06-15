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
        user_answer = int(prompt.integer('You answer: '))

        for num in range(greatest_num, 0, -1):
            if (first_num % num == 0) and (second_num % num == 0)\
                    and (num == user_answer):
                index += 1
                print('Correct!')
                break
            elif (first_num % num == 0) and (second_num % num == 0)\
                    and (num != user_answer):
                return print(f"'{user_answer}' is wrong answer ;(."
                             f"Correct answer was '{num} '"
                             f"\nLet's try again, {name}")

    return print(f'Congratulations, {name}!')

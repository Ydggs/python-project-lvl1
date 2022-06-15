from random import randint
import prompt
from .cli import welcome_user


def even():

    name = welcome_user()
    count = 0

    print('Answer "yes" if the number is even, otherwise answer "no".')

    while count <= 3:

        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ')

        if random_number % 2 == 0:
            true_answer = 'yes'
        else:
            true_answer = 'no'

        if (random_number % 2 == 0 and user_answer == true_answer) \
                or (random_number % 2 != 0 and user_answer == true_answer):

            print('Correct!')
            count += 1
            continue

        else:
            return print(f"'{user_answer}' is wrong answer ;(."
                         f"Correct answer was '{true_answer} '"
                         f"\nLet's try again, {name}")

    return print(f'Congratulations, {name}!')

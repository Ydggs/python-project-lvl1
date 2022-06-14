#!/usr/bin/env python
from random import randint
from ..cli import welcome_user


def main():
    name = welcome_user()
    print(f'Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count != 3:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ')
        if (random_number % 2 == 0 and user_answer == 'yes') or (random_number % 2 != 0 and user_answer == 'no'):
            print('Correct!')
            count += 1
        else:
            print(f"Correct answer was 'no'.Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

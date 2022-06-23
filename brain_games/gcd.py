from .cli import welcome_user, start_game, is_answer
import prompt
import random


def start_gcd():
    name = welcome_user()
    start_game(gcd, name, 2)


def gcd(name):
    first_num = random.randint(1, 100)
    second_num = random.randint(1, 100)

    print(f'Question: {first_num} {second_num}')

    while first_num != second_num:
        if first_num > second_num:
            first_num -= second_num
        else:
            second_num -= first_num

    true_answer = first_num

    user_answer = int(prompt.integer('You answer: '))

    if is_answer(user_answer, true_answer):
        print('Correct!')
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(."
              f"Correct answer was '{true_answer} '")
        print(f"Let's try again, {name}!")
        return False

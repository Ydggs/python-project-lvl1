from .cli import is_answer, is_prime, start_game, welcome_user
import random
import prompt


def start_prime():
    name = welcome_user()
    print('Answer "yes" if given number is prime. otherwise answer "no".')
    start_game(prime, name, 2)


def prime(name):
    random_number = random.randint(2, 100)
    true_answer = is_prime(random_number)

    print(f'Question: {random_number}')
    user_answer = ''

    while user_answer != 'yes' and user_answer != 'no':
        user_answer = prompt.string('You answer: ')

    if is_answer(true_answer, user_answer):
        print('Correct!')
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(."
              f"Correct answer was '{true_answer} '")
        print(f"Let's try again, {name}!")
        return False

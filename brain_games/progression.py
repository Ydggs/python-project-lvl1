from .cli import is_answer, get_progression, arr_to_string, \
    change_value, start_game, welcome_user
import random
import prompt


def start_progression():
    name = welcome_user()
    print('What number is missing in the progression?')
    start_game(progression, name, 2)


def progression(name):
    list_progression = get_progression()

    random_num = random.randint(0, len(list_progression))

    list_progression, true_answer = \
        change_value(list_progression, '..', random_num)

    list_progression = arr_to_string(list_progression)

    print(f'Question: {list_progression}')

    user_answer = prompt.integer('You answer: ')

    if is_answer(true_answer, user_answer):
        print('Correct!')
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(."
              f"Correct answer was '{true_answer} '")
        print(f"Let's try again, {name}!")
        return False

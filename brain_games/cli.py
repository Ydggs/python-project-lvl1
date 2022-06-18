import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def start_game(func, text, count_game):
    back_func = func(text)
    if count_game == 0:
        print(f'Congratulations, {text}!')
        return
    elif is_true(back_func):
        return start_game(func, text, count_game - 1)
    else:
        return


def is_true(text):
    return True if text else False

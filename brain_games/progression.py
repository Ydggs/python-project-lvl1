from .cli import welcome_user
import random
import prompt


def progression():

    name = welcome_user()
    index = 0

    print('What number is missing in the progression?')

    while index < 3:
        random_progressive_size = random.randint(5, 10)
        random_num = random.randint(1, random_progressive_size)
        random_application = random.randint(1, 5)
        first_meaning = random.randint(0, 20)
        progressive_list = ''
        acc = first_meaning
        true_answer = 0

        for num in range(0, random_progressive_size + 1):
            if num == random_num:
                true_answer = acc
                acc += random_application
                progressive_list += '.. '
                continue

            progressive_list += f'{acc} '
            acc += random_application

        print(f'Question: {progressive_list}')

        user_answer = prompt.integer('You answer: ')

        if true_answer == user_answer:
            print('Correct!')
            index += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{true_answer} '")
            return print(f"Let's try again, {name}")

    return print(f'Congratulations, {name}!')

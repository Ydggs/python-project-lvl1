from .cli import welcome_user
import random
import prompt


def prime():
    name = welcome_user()
    index = 0

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    while index < 3:
        random_number = random.randint(2, 100)
        true_answer = ''

        for num in range(2, random_number + 1):
            if random_number % num == 0 and random_number != num:
                true_answer = 'no'
                break
            else:
                true_answer = 'yes'

        print(f'Question: {random_number}', true_answer)
        user_answer = ''

        while user_answer != 'yes' and user_answer != 'no':
            user_answer = prompt.string('You answer: ')

        if user_answer == true_answer:
            print('Correct!')
            index += 1
            continue

        return print(f"'{user_answer}' is wrong answer ;(."
                     f"Correct answer was '{true_answer} '"
                     f"\nLet's try again, {name}")

    return print(f'Congratulations, {name}!')

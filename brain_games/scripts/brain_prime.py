#!/usr/bin/env python3
from ..cli import welcome_user, start_game
from ..prime import prime


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    start_game(prime, name, 2)


if __name__ == '__main__':
    main()

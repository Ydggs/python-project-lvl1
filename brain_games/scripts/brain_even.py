#!/usr/bin/env python3
from ..cli import welcome_user, start_game
from ..even import even


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    start_game(even, name, 2)


if __name__ == '__main__':
    main()

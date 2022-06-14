#!/usr/bin/env python
from ..cli import welcome_user


def main():
    print(f'Welcome to the Brain Games!')
    name = welcome_user()
    print(f'Hello, {name}!')


if __name__ == '__main__':
    main()

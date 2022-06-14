#!/usr/bin/env python
from ..cli import welcome_user


def brain_welcome():
    name = welcome_user()
    print(f'Welcome to the Brain Games! {name}!')


if __name__ == '__main__':
    brain_welcome()

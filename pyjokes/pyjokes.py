from random import choice
from .jokes import jokes


def get_local_joke():
    return choice(jokes)

if __name__ == '__main__':
    print(get_local_joke())

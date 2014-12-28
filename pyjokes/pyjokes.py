from __future__ import absolute_import
import random
from .jokes import jokes


def get_local_joke():
    return random.choice(jokes)


if __name__ == '__main__':
    print(get_local_joke())

from __future__ import absolute_import
import random
from .geek  import geek_neutral, geek_explicit
from .chuck import chuck_neutral, chuck_explicit, chuck_nerdy


def join_joke_sets(joke_sets):
    jokes_set = set(joke_sets)
    jokes     = []
    try:
        for set_name in jokes_set:
            jokes.extend(eval(set_name))
        return jokes
    except:
        print('Could not find joke set {}.'.format(set_name))
        raise


def get_local_joke(joke_sets=['geek_neutral']):
    jokes = join_joke_sets(joke_sets)
    return random.choice(jokes)


if __name__ == '__main__':
    print(get_local_joke())

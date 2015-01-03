from __future__ import absolute_import
import random
from .jokes import geek_neutral, geek_explicit, chuck_nerdy

def get_joke(category='neutral'):
    jokes = {
        'neutral': geek_neutral,
        'explicit': geek_explicit,
        'chuck': chuck_nerdy,
        'all': geek_neutral + geek_explicit + chuck_nerdy,
    }[category]
    return random.choice(jokes)


if __name__ == '__main__':
    print(get_joke('all'))

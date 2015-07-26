from __future__ import absolute_import
import random
from .jokes import neutral, explicit, chuck

def get_joke(category='neutral'):
    jokes = {
        'neutral': neutral,
        'explicit': explicit,
        'chuck': chuck,
        'all': neutral + explicit + chuck,
    }[category]
    return random.choice(jokes)

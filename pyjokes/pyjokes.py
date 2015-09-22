from __future__ import absolute_import
import random

def get_joke(category='neutral', language='eng'):
    """
    Parameters
    ----------
    category: str
        Choices: 'neutral', 'explicit', 'chuck', 'all'
    lang: str
        Choices: 'eng', 'de', 'spa'

    Returns
    -------
    joke: str
    """

    if language == 'eng':
        from .jokes_eng import jokes
    elif language == 'de':
        from .jokes_de import jokes
    elif language == 'spa':
        from .jokes_spa import jokes

    try:
        jokes = jokes[category]
    except:
        return 'Could not get the joke. Choose another category.'
    else:
        return random.choice(jokes)

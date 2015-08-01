from __future__ import absolute_import
import random
import importlib

def get_joke(category='neutral', language='en'):
    """
    Parameters
    ----------
    category: str
        Choices: 'neutral', 'explicit', 'chuck', 'all'
    lang: str
        Choices: 'en', 'de', 'es'

    Returns
    -------
    joke: str
    """

    if language == 'en':
        from .jokes_en import jokes
    elif language == 'de':
        from .jokes_de import jokes
    elif language == 'es':
        from .jokes_es import jokes

    try:
        jokes = jokes[category]
    except:
        return 'Could not get the joke. Choose another category.'
    else:
        return random.choice(jokes)

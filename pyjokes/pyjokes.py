from __future__ import absolute_import
import random

from .jokes_en import jokes as jokes_en
from .jokes_de import jokes as jokes_de
from .jokes_es import jokes as jokes_es


all_jokes = {
    'en': jokes_en,
    'de': jokes_de,
    'es': jokes_es,
}


class LanguageNotFoundError(Exception):
    pass


class CategoryNotFoundError(Exception):
    pass


def _get_jokes(language='en', category='neutral', singular=True):
    if language in all_jokes:
        jokes = all_jokes[language]
    else:
        raise LanguageNotFoundError('No such language %s' % language)

    if category in jokes:
        jokes = jokes[category]
        if singular:
            return random.choice(jokes)
        else:
            return jokes
    else:
        raise CategoryNotFound('No such category %s' % category)



def get_joke(language='en', category='neutral'):
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

    return _get_jokes(language, category, singular=True)

def get_jokes(language='en', category='neutral'):
    """
    Parameters
    ----------
    category: str
        Choices: 'neutral', 'explicit', 'chuck', 'all'
    lang: str
        Choices: 'en', 'de', 'es'

    Returns
    -------
    jokes: list
    """

    return _get_jokes(language, category, singular=False)

from __future__ import absolute_import
import random

from .jokes_en import jokes_en
from .jokes_de import jokes_de
from .jokes_es import jokes_es


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
    if language not in all_jokes:
        raise LanguageNotFoundError('No such language %s' % language)

    jokes = all_jokes[language]

    if category not in jokes:
        raise CategoryNotFound('No such category %s' % category)

    jokes = jokes[category]

    if singular:
        return random.choice(jokes)
    else:
        return jokes


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

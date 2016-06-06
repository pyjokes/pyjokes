from __future__ import absolute_import
import random

from .jokes_en import jokes_en
from .jokes_de import jokes_de
from .jokes_es import jokes_es
from .jokes_gl import jokes_gl
from .jokes_eu import jokes_eu

all_jokes = {
    'en': jokes_en,
    'de': jokes_de,
    'es': jokes_es,
    'gl': jokes_gl,
    'eu': jokes_eu,
}


class LanguageNotFoundError(Exception):
    pass


class CategoryNotFoundError(Exception):
    pass


def get_jokes(language='en', category='neutral'):
    """
    Parameters
    ----------
    category: str
        Choices: 'neutral', 'adult', 'chuck', 'all'
    lang: str
        Choices: 'en', 'de', 'es', 'gl', 'eu'

    Returns
    -------
    jokes: list
    """

    if language not in all_jokes:
        raise LanguageNotFoundError('No such language %s' % language)

    jokes = all_jokes[language]

    if category not in jokes:
        raise CategoryNotFoundError('No such category %s in language %s' % (category, language))

    return jokes[category]


def get_joke(language='en', category='neutral'):
    """
    Parameters
    ----------
    category: str
        Choices: 'neutral', 'adult', 'chuck', 'all'
    lang: str
        Choices: 'en', 'de', 'es', 'gl', 'eu'

    Returns
    -------
    joke: str
    """

    jokes = get_jokes(language, category)
    return random.choice(jokes)

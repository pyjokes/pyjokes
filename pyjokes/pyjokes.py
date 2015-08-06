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

    if language in all_jokes:
        jokes = all_jokes[language]
    else:
        raise LanguageNotFoundError('No such language %s' % language)

    if category in jokes:
        jokes = jokes[category]
        return random.choice(jokes)
    else:
        raise CategoryNotFound('No such category %s' % category)

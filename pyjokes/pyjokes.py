from __future__ import absolute_import
import random

from .jokes_en import jokes_en
from .jokes_de import jokes_de
from .jokes_es import jokes_es
from .jokes_fr import jokes_fr
from .jokes_gl import jokes_gl
from .jokes_eu import jokes_eu
from .jokes_it import jokes_it
from .jokes_cs import jokes_cs
from .jokes_pl import jokes_pl
from .jokes_lt import jokes_lt
from .jokes_hu import jokes_hu
from .jokes_fr import jokes_fr
from .jokes_se import jokes_se
from .jokes_ru import jokes_ru

all_jokes = {
    'en': jokes_en,
    'de': jokes_de,
    'es': jokes_es,
    'fr': jokes_fr,
    'gl': jokes_gl,
    'eu': jokes_eu,
    'it': jokes_it,
    'hu': jokes_hu,
    'fr': jokes_fr,
    'se': jokes_se,
    'ru': jokes_ru,
    'cs': jokes_cs,
    'pl': jokes_pl,
    'lt': jokes_lt,
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
        Choices: 'neutral', 'chuck', 'all', 'twister'
    lang: str
        Choices: 'en', 'de', 'es', 'fr', 'gl', 'eu', 'it', 'hu', 'lt', 'pl', 'cs', 'ru', 'se', 'fr'

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
        Choices: 'neutral', 'chuck', 'all', 'twister'
    lang: str
        Choices: 'en', 'de', 'es', 'fr', 'gl', 'eu', 'it', 'hu', 'lt', 'pl', 'cs', 'ru', 'fr'

    Returns
    -------
    joke: str
    """

    jokes = get_jokes(language, category)
    return random.choice(jokes)

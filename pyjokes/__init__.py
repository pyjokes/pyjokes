from __future__ import absolute_import
from .pyjokes import get_joke
from .jokes import geek_neutral, geek_explicit, chuck_nerdy

jokes = geek_neutral + geek_explicit + chuck_nerdy


__version__ = '0.1.2'

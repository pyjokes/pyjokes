from __future__ import absolute_import
from .pyjokes import get_joke
from .jokes import neutral, explicit, chuck

jokes = neutral + explicit + chuck


__version__ = '0.2.0'

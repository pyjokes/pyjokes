"One line jokes for programmers (jokes as a service)"

from __future__ import absolute_import
from .pyjokes import get_joke, get_jokes


__project__      = 'pyjokes'
__version__      = '0.6.0'
__keywords__     = ['pyjokes', 'pyjokes', 'jokes', 'joke']
__author__       = 'Pyjokes Society'
__author_email__ = 'ben@bennuttall.com'
__url__          = 'https://pyjok.es/'
__platforms__    = 'ALL'

__classifiers__ = [
    "Development Status :: 4 - Beta",
    "Topic :: Utilities",
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
]

__entry_points__ = {
    'console_scripts': [
        'pyjoke = pyjokescli.pyjoke:main',
        'pyjokes = pyjokescli.pyjokes:main',
    ],
}

__requires__ = []

__extra_requires__ = {
    'doc':   ['mkdocs'],
    'test':  ['pytest', 'coverage', 'tox'],
}

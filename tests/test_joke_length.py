from pyjokes.jokes_en import jokes_en
from pyjokes.jokes_de import jokes_de
from pyjokes.jokes_es import jokes_es
from pyjokes.jokes_fr import jokes_fr
from pyjokes.jokes_gl import jokes_gl
from pyjokes.jokes_eu import jokes_eu
from pyjokes.jokes_it import jokes_it
from pyjokes.jokes_sv import jokes_sv
from pyjokes.jokes_tr import jokes_tr


def _test_joke_length(joke):
    assert len(joke) <= 140


def _test_joke_group(jokes):
    for joke in jokes:
        _test_joke_length(joke)


def test_jokes_lengths():
    jokes_sets = [
        jokes_en,
        jokes_es,
        jokes_fr,
        jokes_de,
        jokes_gl,
        jokes_eu,
        jokes_it,
        jokes_sv,
        jokes_tr,
    ]
    for jokes in jokes_sets:
        _test_joke_group(jokes["all"])

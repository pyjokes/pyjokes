from pyjokes.jokes_en import jokes_en
from pyjokes.jokes_de import jokes_de
from pyjokes.jokes_es import jokes_es
from pyjokes.jokes_fr import jokes_fr


def _test_joke_length(joke):
    assert len(joke) <= 140


def _test_joke_group(jokes):
    for joke in jokes:
        _test_joke_length(joke)


def test_jokes_lengths():
    jokes_sets = [jokes_en, jokes_es, jokes_de, jokes_fr]
    for jokes in jokes_sets:
        _test_joke_group(jokes['all'])

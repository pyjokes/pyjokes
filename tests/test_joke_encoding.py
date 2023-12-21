from pyjokes.jokes_en import jokes_en
from pyjokes.jokes_de import jokes_de
from pyjokes.jokes_es import jokes_es
from pyjokes.jokes_fr import jokes_fr
from pyjokes.jokes_gl import jokes_gl
from pyjokes.jokes_eu import jokes_eu
from pyjokes.jokes_it import jokes_it
from pyjokes.jokes_lt import jokes_lt

#test if joke is windows compatible
def _test_joke_win(joke):
    assert len(joke) <= len(joke.encode('iso-8859-1', 'ignore')) ##ascii don't support umlauts

def _test_default_locale(joke):
    import locale
    encod = locale.getdefaultlocale()[1]
    assert len(joke) <= len(joke.encode(encod, 'ignore'))

#unix is full compatible - no need of tests
def test_jokes_lengths():
    jokes_sets = [jokes_en, jokes_es, jokes_fr, jokes_de, jokes_gl, jokes_eu, jokes_it, jokes_lt]
    for jokes in jokes_sets:
        for j in jokes['all']:
            _test_default_locale(j)
            _test_joke_win(j)

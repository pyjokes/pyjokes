from pyjokes.jokes_en import jokes_en
from pyjokes.jokes_de import jokes_de
from pyjokes.jokes_es import jokes_es


#test if joke is windows compatible
def _test_joke_win(joke):
    assert len(joke) <= len(joke.encode('ascii', 'ignore'))

def _test_default_locale(joke):
    import locale
    encod = locale.getdefaultlocale()[1]
    assert len(joke) <= len(joke.encode(encod, 'ignore'))

#unix is full compatible - no need of tests
def test_jokes_lengths():
    jokes_sets = [jokes_en, jokes_es, jokes_de]
    for jokes in jokes_sets:
        for j in jokes['all']:
            _test_default_locale(j)
            _test_joke_win(j)

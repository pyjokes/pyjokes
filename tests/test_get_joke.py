

def test_get_joke():
    from pyjokes import get_joke

    for i in range(10):
        assert get_joke()

    languages = ['eng', 'de', 'spa']
    categories = ['neutral', 'explicit', 'all']

    for lang in languages:
        for cat in categories:
            for i in range(10):
                assert get_joke(cat, lang)

import pytest
from   pyjokes import get_joke
from   pyjokes.pyjokes import LanguageNotFoundError, CategoryNotFoundError


def test_get_joke():
    assert get_joke()

    languages = ['en', 'de', 'es']
    categories = ['neutral', 'explicit', 'all']

    for lang in languages:
        assert get_joke(language=lang)

    for cat in categories:
        assert get_joke(category=cat)


def test_get_joke_raises():
    assert pytest.raises(LanguageNotFoundError, get_joke, language='eu')

    assert pytest.raises(LanguageNotFoundError, get_joke, language='tr')

    assert pytest.raises(CategoryNotFoundError, get_joke, category='123')
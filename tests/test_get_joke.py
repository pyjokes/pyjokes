import pytest
from pyjokes import get_joke, get_jokes
from pyjokes.pyjokes import LanguageNotFoundError, CategoryNotFoundError


languages = ['en', 'de', 'es', 'gl', 'eu', 'it', 'hu']
categories = ['neutral', 'all']
test_data = ['', 'abc', '123']


def test_get_joke():
    assert get_joke()

    for language in languages:
        assert get_joke(language=language)

    for category in categories:
        assert get_joke(category=category)


def test_get_joke_with_language_raises():
    for language in test_data:
        assert pytest.raises(
            LanguageNotFoundError, get_joke, language=language
        )


def test_get_joke_with_category_raises():
    for category in test_data:
        assert pytest.raises(
            CategoryNotFoundError, get_joke, category=category
        )


def test_get_joke_in_language_with_category_raises():
    for category in test_data:
        assert pytest.raises(
            CategoryNotFoundError, get_joke,
            language='en', category=category
        )

def test_all_jokes_are_funny():
    for language in languages:
        jokes = get_jokes(language=language, category='all')
        for joke in jokes:
            assert True

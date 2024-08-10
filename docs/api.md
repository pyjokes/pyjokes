# API Reference

Import the pyjokes module to access `pyjokes` in any Python application:

```python
import pyjokes
```

## pyjokes.get_joke()

Returns a random joke from the given category in the given language.

| Parameters | Types | Values | Default |
| ---------- | ----- | ------ | ------- |
| `language` | `str` | See `LANGUAGES` | `en` |
| `category` | `str` | See `CATEGORIES` | `neutral` |

Return type: `str`

If the `language` value provided is not available, a `LanguageNotFoundError` exception is raised.

If the `category` value provided is not available, a `CategoryNotFoundError` exception is raised.

## pyjokes.get_jokes()

Returns a list of jokes from the given category in the given language.

Takes the same parameters as `get_joke()`.

Return type: `list[str]`

## pyjokes.forever()

A generator which yields jokes.

Takes the same parameters as `get_joke()`.

Yield type: `str`

## Supported languages

These are all the languages supported by pyjokes:

| Language   | Value (ISO 639 two-letter language code) |
| ---------- | ---- |
| Basque     | `cs` |
| German     | `de` |
| English    | `en` |
| Spanish    | `es` |
| Basque     | `eu` |
| French     | `fr` |
| Galician   | `gl` |
| Hungarian  | `hu` |
| Italian    | `it` |
| Lithuanian | `lt` |
| Polish     | `pl` |
| Russian    | `ru` |
| Swedish    | `sv` |

To add support for another language, please see the [contributing page](https://github.com/pyjokes/pyjokes/blob/main/CONTRIBUTING.md).

## Joke categories

Joke categories are:

| Category name | Value     | Notes |
| ------------- | --------- | ----- |
| Neutral       | `neutral` | Standard programmer jokes     |
| Chuck Norris  | `chuck`   | Chuck Norris programmer jokes |
| All           | `all`     | All joke categories combined  |

## Exceptions

Exceptions are available at `pyjokes.exc`:

- `PyjokesError` (base class for all library exceptions)
- `LanguageNotFoundError`
- `CategoryNotFoundError`
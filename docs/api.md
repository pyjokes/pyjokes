# API Reference

Import the pyjokes module to access `pyjokes` in any Python application:

```python
import pyjokes
```

## pyjokes.get_joke()

Returns a random joke from the given category in the given language.

| Parameters | Types | Values | Default |
| ---------- | ----- | ------ | ------- |
| language   | str   | 'en', 'de', 'es' | 'en' |
| category   | str   | 'neutral', 'adult', 'chuck', 'all' | 'neutral' |

Return type: str

If the `language` value provided is not available, a `LanguageNotFoundError` exception is raised.

If the `category` value provided is not available, a `CategoryNotFoundError` exception is raised.

## pyjokes.get_jokes()

Returns a list of jokes from the given category in the given language.

| Parameters | Types | Values | Default |
| ---------- | ----- | ------ | ------- |
| language   | str   | 'en', 'de', 'es' | 'en' |
| category   | str   | 'neutral', 'adult', 'chuck', 'all' | 'neutral' |

Return type: list

If the `language` value provided is not available, a `LanguageNotFoundError` exception is raised.

If the `category` value provided is not available, a `CategoryNotFoundError` exception is raised.

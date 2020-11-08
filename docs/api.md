# API Reference

Import the pyjokes module to access `pyjokes` in any Python application:

```python
import pyjokes
```

## pyjokes.get_joke()

Returns a random joke from the given category in the given language.

| Parameters | Types | Values | Default |
| ---------- | ----- | ------ | ------- |
| language   | str   | 'en', 'de', 'es', 'gl' , 'eu', 'it'| 'en' |
| category   | str   | 'neutral', 'chuck', 'all' | 'neutral' |

Return type: str

If the `language` value provided is not available, a `LanguageNotFoundError` exception is raised.

If the `category` value provided is not available, a `CategoryNotFoundError` exception is raised.

## pyjokes.get_jokes()

Returns a list of jokes from the given category in the given language.

| Parameters | Types | Values | Default |
| ---------- | ----- | ------ | ------- |
| language   | str   | 'en', 'de', 'es', 'gl', 'eu', 'it' | 'en' |
| category   | str   | 'neutral', 'chuck', 'all' | 'neutral' |

Return type: list

If the `language` value provided is not available, a `LanguageNotFoundError` exception is raised.

If the `category` value provided is not available, a `CategoryNotFoundError` exception is raised.

## Supported languages

These are all the languages supported by pyjokes:

| Language   | Value | 
| ---------- | ----- | 
| Basque     | 'eu'  | 
| English    | 'en'  | 
| Galician   | 'gl'  | 
| German     | 'de'  | 
| Italian    | 'it'  |
| Spanish    | 'es'  | 

To add support for another language, please see the [contributing page](https://github.com/pyjokes/pyjokes/blob/master/CONTRIBUTING.md).

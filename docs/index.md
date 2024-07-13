# pyjokes

One line jokes for programmers (jokes as a service)

![pyjokes](images/pyjokes.png)

## Install

Install with pip:

```bash
pip install pyjokes
```

See the [install](install.md) page for information on installing on different platforms.

## Usage

### Command line

Run `pyjoke` or `pyjokes` at the command line to get a random joke:

```
$ pyjoke
Why did the programmer quit his job? Because he didn't get arrays.
```

### Python

Import the `pyjokes` module in a Python file and use the `get_joke` function to easily access a
random joke into your application:

```python
import pyjokes

print(pyjokes.get_joke())
```

See the [API reference](api.md) for full documentation.

## Proposal of new jokes

New jokes should be proposed in the [proposal issue](https://github.com/pyjokes/pyjokes/issues/10)
or via pull request.

## Reference

- [GitHub](https://github.com/pyjokes/pyjokes)
- [PyPI](https://pypi.org/project/pyjokes)
- [Twitter](https://twitter.com/pyjokes_bot)

## PyJokes logo

The logo was designed by [Sam Alder](https://samalder.co.uk/). The PyJokes Society is eternally
grateful for his contribution.
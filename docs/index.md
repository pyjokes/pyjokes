# pyjokes

One line jokes for programmers (jokes as a service)

[![](images/pyjokes.png)](images/pyjokes_logo.png)

## Installation

Install the `pyjokes` module with pip:

```console
pip3 install pyjokes
```

## Usage

Once installed, simply call `pyjoke` or `pyjokes` from the command line:

```console
$ pyjoke
Why do Java programmers have to wear glasses? Because they don't see sharp.
```

Or add it to your `.bashrc` or `.zshrc` file to see a joke every time you open a terminal!

You can also access the jokes in your own project by importing `pyjokes` and using the function
`get_joke`:

```pycon
>>> import pyjokes
>>> print(pyjokes.get_joke())
Why do programmers confuse Halloween with Christmas? Because OCT 31 == DEC 25.
```

We support many languages, and have multiple joke categories:

```pycon
>>> import pyjokes
>>> print(pyjokes.get_joke("eu"))  # basque joke
Zer dira 8 Bocabits? BocaByte bat
>>> print(pyjokes.get_joke("es", "chuck"))  # spanish chuck norris joke
El teclado de Chuck Norris no tiene tecla F1, es el ordenador el que le pide ayuda a él.
```

There is also a `get_jokes` function which returns all the jokes in the given language and category:

```python
import pyjokes

for joke in pyjokes.get_jokes():
    print(joke)
```

Alternatively, use the `pyjokes.forever` generator function:

```python
import pyjokes

for joke in pyjokes.forever():
    # This will go on forever... you're welcome.
    print(joke)
```

## Maintainers

The project is maintained by the members of the PyJokes Society:

- Ben Nuttall
- Alex Savio
- Borja Ayerdi
- Oier Etxaniz ([RIP](https://www.europython-society.org/farewell-to-oier-echaniz-beneitez))

## Contributing

- The code is licensed under the [BSD Licence](http://opensource.org/licenses/BSD-3-Clause)
- Please use GitHub issues to submit bugs and report issues
- Feel free to contribute to the code
- Feel free to contribute jokes (via pull request or [proposal issue](https://github.com/pyjokes/pyjokes/issues/10))
- See the [contributing policy](https://github.com/pyjokes/pyjokes/tree/main/CONTRIBUTING.md)

## PyJokes logo

The [logo](images/pyjokes_logo.png) was designed by [Sam Alder](https://samalder.co.uk/). The
PyJokes Society is eternally grateful for his contribution.
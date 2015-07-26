# pyjokes

Pyjokes is a Python module for one-line programmer jokes. `pip install pyjokes` and run `pyjoke`. Pyjokes was founded at [PySS14](http://pyss.org/) and directed by the [Pyjokes Society](https://github.com/pyjokes).

## Pyjokes Society

Founders:

- [Ben Nuttall](https://github.com/bennuttall) - Chairperson
- [Alex Savio](https://github.com/alexsavio) - Vice-chairperson
- [Borja Ayerdi](https://github.com/borjaayerdi) - Treasurer
- [Oier Etxaniz](https://github.com/oiertwo) - Spokesperson

See members on the [wiki](https://github.com/pyjokes/pyjokes/wiki).

## Installation

Install with `pip`:

```bash
sudo pip install pyjokes
```

## Usage

Command line usage:

```bash
pyjoke
```

## API reference

Import the pyjokes module to access `pyjokes` in any Python application:

```python
import pyjokes
```

### Functions

#### pyjokes.get_joke()

**Arguments:**

`category` - Default: 'neutral', Options: 'explicit', 'chuck', 'all'

### jokes lists

The following jokes lists are available:

- `neutral` (neutral jokes)
- `explicit` (explicit jokes)
- `chuck` (Chuck Norris themed jokes)

Example usage:

```python
import pyjokes
import random

print(random.choice(pyjokes.neutral))
```

## Proposal of new jokes

New jokes should be proposed in the [proposal issue](https://github.com/pyjokes/pyjokes/issues/10) or via pull request.

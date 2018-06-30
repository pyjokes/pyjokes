.. image:: https://travis-ci.org/pyjokes/pyjokes.svg
    :target: https://travis-ci.org/pyjokes/pyjokes
.. image:: https://coveralls.io/repos/pyjokes/pyjokes/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/pyjokes/pyjokes?branch=master

=======
pyjokes
=======

One line jokes for programmers (jokes as a service)

Installation
============

Install the `pyjokes` module with pip.

See the `documentation`_ for installation instructions.

Usage
=====

Once installed, simply call `pyjoke` from the command line or add it to your .bashrc file to see a joke everytime you start a terminal session.

Use the `-c` flag to get jokes from a specific category. Options::

    -c neutral [default] (neutral geek jokes)
    -c chuck (Chuck Norris geek jokes)
    -c all (all jokes)
    -c twister (Tongue-twister)

You can also access the jokes in your own project by importing `pyjokes` and using the functions `get_joke` and `get_jokes`

Comprehensive documentation is available at http://pyjok.es

Contributors
============

Development:

* `Ben Nuttall`_
* `Alex Savio`_
* `Borja Ayerdi`_
* `Oier Etxaniz`_

Jokes:

* `Luke Wren`_
* `Sarah Bird`_
* `Yash Mehrotra`_
* `Marc Kirkwood`_
* `Gregory Parker`_
* `Martin O'Hanlon`_
* `Graham Markall`_
* `Andreas Reinle`_
 

Contributing
============

* The code is licensed under the `BSD Licence`_
* The project source code is hosted on `GitHub`_
* Please use `GitHub issues`_ to submit bugs and report issues
* Feel free to `contribute`_ to the code
* Feel free to contribute jokes (via pull request or `proposal issue`_)
* See the `contributing policy`_ on GitHub

Tests
=====

Install requirements (pytest)

Run tests::

    python setup.py test

Pyjokes Society
===============

This project was founded at `PySS 2014`_ and is directed by the `Pyjokes Society`_.


.. _documentation: http://pyjok.es/install/
.. _http://pyjok.es: http://pyjok.es/
.. _Ben Nuttall: https://github.com/bennuttall
.. _Alex Savio: https://github.com/alexsavio
.. _Borja Ayerdi: https://github.com/borjaayerdi
.. _Oier Etxaniz: https://github.com/oiertwo
.. _Luke Wren: https://github.com/wren6991
.. _Sarah Bird: https://github.com/birdsarah
.. _Yash Mehrotra: https://github.com/yashmehrotra
.. _Marc Kirkwood: https://github.com/trojjer
.. _Gregory Parker: https://github.com/ElectronicsGeek
.. _Martin O'Hanlon: https://github.com/martinohanlon
.. _Graham Markall: https://github.com/gmarkall
.. _BSD Licence: http://opensource.org/licenses/BSD-3-Clause
.. _GitHub: https://github.com/pyjokes/pyjokes
.. _GitHub Issues: https://github.com/pyjokes/pyjokes/issues
.. _contribute: https://github.com/pyjokes/pyjokes/tree/master/CONTRIBUTING.md
.. _proposal issue: https://github.com/pyjokes/pyjokes/issues/10
.. _contributing policy: https://github.com/pyjokes/pyjokes/tree/master/CONTRIBUTING.md
.. _PySS 2014: http://www.pyss.org/
.. _Pyjokes Society: http://pyjok.es/society/

.. image:: https://travis-ci.org/pyjokes/pyjokes.svg
    :target: https://travis-ci.org/pyjokes/pyjokes
    
=======
pyjokes
=======

One line jokes for programmers (jokes as a service)

Installation
============

Install the `pyjokes` module with pip.

Python 3::

    sudo apt-get install python3-pip
    sudo pip3 install pyjokes

or on some systems::

    sudo apt-get install python3-pip
    sudo pip-3.2 install pyjokes

Python 2::

    sudo apt-get install python-pip
    sudo pip install pyjokes

Usage
=====

Once installed, simply call `pyjoke` from the command line.

Alternatively use the `-c` flag to get jokes from a specific category. Options::

    -c neutral [default] (neutral geek jokes)
    -c explicit (explicit geek jokes)
    -c chuck (Chuck Norris geek jokes)
    -c all (all jokes)

You can also access the jokes in your own project by importing `pyjokes`. You have access to the `get_joke` function, the `jokes` list, and the joke catgeory lists separately: `geek_neutral`, `geek_explicit`, `chuck_nerdy`.

Contributors
============

* `Ben Nuttall`_
* `Alex Savio`_
* `Borja Ayerdi`_

Contributing
============

New jokes should be proposed in the `proposal issue`_ or via pull request.

Pyjokes Society
===============

This project is directed by the `Pyjokes Society`_

Open Source
===========

* The code is licensed under the `BSD Licence`_
* The project source code is hosted on `GitHub`_
* Please use `GitHub issues`_ to submit bugs and report issues
* Feel free to contribute!


.. _Ben Nuttall: https://github.com/bennuttall
.. _Alex Savio: https://github.com/alexsavio
.. _Borja Ayerdi: https://github.com/borjaayerdi
.. _proposal issue: _https://github.com/pyjokes/pyjokes/issues/10
.. _Pyjokes Society: https://github.com/pyjokes/society
.. _PySS 2014: http://www.pyss.org/
.. _BSD Licence: http://opensource.org/licenses/BSD-3-Clause
.. _GitHub Issues: https://github.com/pyjokes/pyjokes
.. _GitHub: https://github.com/pyjokes/pyjokes/issues

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="pyjokes",
    version="0.1.2",
    author="Ben Nuttall",
    author_email="ben@raspberrypi.org",
    description="One line jokes for programmers (jokes as a service)",
    license="BSD",
    keywords=[
        "pyjokes",
        "jokes",
    ],
    url="https://github.com/bennuttall/pyjokes",
    packages=[
        "pyjokes",
    ],
    long_description=read('README.rst'),
    scripts=['scripts/pyjoke'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)

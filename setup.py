import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="pyjokes",
    version="0.2.0",
    author="Pyjokes Society",
    description="One line jokes for programmers (jokes as a service)",
    license="BSD",
    keywords=[
        "pyjokes",
        "jokes",
    ],
    url="https://github.com/pyjokes/pyjokes",
    packages=find_packages(),
    long_description=read('README.rst'),
    scripts=['scripts/pyjoke'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
)

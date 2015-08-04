import os
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    name="pyjokes",
    version="0.2.1",
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
    scripts=['scripts/pyjoke',
             'scripts/pyjokes'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    #test requirements and class specification:
    test_require=['pytest'],
    cmdclass={ 'test' : PyTest },
)

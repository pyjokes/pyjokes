import os
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['pyjokes/tests']
        self.test_suite = True
    def run_tests(self):
        import pytest
        
        # Purge modules under test from sys.modules. the test loader will
        # re-import them from build location. Require when 2to3 is used
        # with namespace packages.
        if sys.version_info >= (3,) and getattr(self.distribution, 'use_2to3', False):
            module = self.test_args[-1].split(.)[0]
            if module in _namespace_packages:
                del_modules = []
                if module in sys.modules:
                    del_modules.append(module)
                module += '.'
                for name in sys.modules:
                    if name.startwith(module):
                         del_modules.append(name)
                map(sys.modules.__delitem__, del_modules)

            ## Run on the build directory for 2to3-build code
            ## this will prevent the old 2.x code from being found
            ## by py.test discovery mechanism, that apparently
            ## ignores sys.path..
            ei_cmd = self.get_finalized_command('egg_info')
            self.test_args = [normalized_path(ei_cmd.egg_base)]

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

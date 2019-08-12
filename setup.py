"Setup script for the pyjokes package"

import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import os


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def main():
    "Executes setup when this script is the top-level"
    import pyjokes as app

    setup(
        name=app.__project__,
        version=app.__version__,
        description=app.__doc__,
        long_description=read('README.rst'),
        classifiers=app.__classifiers__,
        author=app.__author__,
        author_email=app.__author_email__,
        url=app.__url__,
        license=[
            c.rsplit('::', 1)[1].strip()
            for c in app.__classifiers__
            if c.startswith('License ::')
        ][0],
        keywords=app.__keywords__,
        packages=find_packages(),
        include_package_data=True,
        platforms=app.__platforms__,
        entry_points=app.__entry_points__,
        tests_require=app.__test_requires__,
        cmdclass={
            'test': PyTest
        },
    )

if __name__ == '__main__':
    main()

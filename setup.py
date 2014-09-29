# -*- coding: utf-8 -*-

import os
import setuptools


setuptools.setup(
    name="pyjokes",
    version="0.1.0",
#    url="",

    author="",
    author_email="",

    description="",
    long_description=open('README.md').read(),

    packages=setuptools.find_packages(),

    #install_requires=[str(ir.req) for ir in install_reqs],

    #extra_files=['CHANGES.rst', 'LICENSE', 'README.rst'],

    scripts=['scripts/pyjoke'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)

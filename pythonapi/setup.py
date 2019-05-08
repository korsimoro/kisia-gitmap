#!/usr/bin/env python

from distutils.core import setup

setup(
    name='kit-api-gitmap',
    version='0.1',
    description='KISIA Python Toolkit',
    author='Korsimoro',
    author_email='eric@korsimoro.com',
    url='none-yet',
    packages=[
		'gitmap'
		],
    install_requires=[
		"json-spec",
		"python-slugify",
		"PyGitHub"
    ],
    entry_points = {
    }
)

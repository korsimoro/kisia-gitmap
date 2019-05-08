#!/usr/bin/env python

from distutils.core import setup

setup(
    name='kit-cli-gitmap',
    version='0.1',
    description='KIT-Workbench Pluggable CLI',
    author='Korsimoro',
    author_email='eric@korsimoro.com',
    url='none-yet',
    packages=[
		'kit.gitmap'
		],
    install_requires=[
        'click',
        'gitpython'
    ],
    entry_points = {
        'console_scripts': ['kitcli=kit.gitmap:cli'],
    }
)

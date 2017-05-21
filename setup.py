#!/usr/bin/env python

import distutils.core

distutils.core.setup(
    name='lanbox',
    version='1.0',
    url='https://github.com/bit/python-lanbox',
    description='python interface for your LanBox controller',
    author='j',
    author_email='j@mailb.org',
    license='GPL',
    packages=['lanbox'],
    install_requires=['six>=1.5.2'],
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

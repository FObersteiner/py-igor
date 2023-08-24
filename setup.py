#!/usr/bin/env python
import sys
from distutils.core import setup

import igor

if len(sys.argv) == 1:
    sys.argv.append("install")

dist = setup(
    name="igor.py",
    version=igor.__version__,
    author="Paul Kienzle",
    author_email="paul.kienzle@nist.gov",
    url="https://github.com/reflectometry/igor.py",
    description="Read Igor Pro files from python",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: Public Domain",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    py_modules=["igor"],
)

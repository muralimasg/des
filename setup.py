#!/usr/bin/env python
# encoding: utf-8

import sys
from setuptools import setup

version = "1.0.4"

description = (
    "A pure Python implementation for the famous DES algorithm"
)

if sys.version_info < (3, ):
    kw = {}
else:
    kw = {"encoding": "utf-8"}

with open("README.md", **kw) as f:
    long_description = f.read()


classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Security",
    "Topic :: Security :: Cryptography",
]

setup(
    name="des",
    version=version,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="Eric Wong",
    author_email="ericwong@zju.edu.cn",
    url="https://github.com/littlefisher/des",
    packages=["des"],
    classifiers=classifiers,
)

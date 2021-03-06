#!/usr/bin/env python

import os.path
import hearthstone
from setuptools import setup, find_packages


README = open(os.path.join(os.path.dirname(__file__), "README.md")).read()

CLASSIFIERS = [
	"Development Status :: 4 - Beta",
	"Intended Audience :: Developers",
	"License :: OSI Approved :: MIT License"
	"Programming Language :: Python",
	"Programming Language :: Python :: 3",
	"Programming Language :: Python :: 3.4",
	"Topic :: Games/Entertainment :: Simulation",
]

setup(
	name="hearthstone",
	version=hearthstone.__version__,
	packages=find_packages(),
	author=hearthstone.__author__,
	author_email=hearthstone.__email__,
	description="CardDefs.xml parser and Hearthstone enums for Python applications",
	classifiers=CLASSIFIERS,
	download_url="https://github.com/HearthSim/python-hearthstone/tarball/master",
	long_description=README,
	license="MIT",
	url="https://github.com/HearthSim/python-hearthstone",
)

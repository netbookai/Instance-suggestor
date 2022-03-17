#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
import os

def get_version(version_tuple):
    if not isinstance(version_tuple[-1], int):
        return '.'.join(
            map(str, version_tuple[:-1])
        ) + version_tuple[-1]
    return '.'.join(map(str, version_tuple))

# path to the packages __init__ module in project source tree
init = os.path.join(os.path.dirname(__file__), 'src', 'InstanceSuggestor','__init__.py')
version_line = list(filter(lambda l: l.startswith('VERSION'), open(init)))[0]
PKG_VERSION = get_version(eval(version_line.split('=')[-1]))

setup(
	author = 'Shruti Sharma',
	author_email = "shruti.sharma@netbook.ai",
	classifiers = [
	'Programming Language :: Python',
	'Programming Language :: Python :: 3',
	"Operating System :: OS Independent",],
	description = "A cloud instance suggestor",
	long_description=open('README.md').read(),
	long_description_content_type="text/markdown",
	name = 'InstanceSuggestor',
	version = PKG_VERSION,
	zip_safe = False,
	license = 'LICENSE.txt',
	url = 'https://github.com/NetBook-ai/Instance-suggestor',
	packages=find_packages('src'),
	package_dir = {'':'src'},
	install_requires=['numpy', 'pandas'],
	)


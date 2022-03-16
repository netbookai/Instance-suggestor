#!/usr/bin/env python
# coding: utf-8

from .InstanceSuggestor import *
from .suggest import *

# version as tuple for simple comparisons 
VERSION = (1, 1, 2)

# string created from tuple to avoid inconsistency 
__version__ = ".".join([str(x) for x in VERSION])
__author__ = 'Shruti Sharma'
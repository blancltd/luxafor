"""
Luxafor Python Interface

The API is close to the hardware features.
"""
from .api import API
# pylint: disable=wildcard-import
from .constants import *
# Normally you don't want to import *, but in this case these are all constants.

from .luxafor import Luxafor

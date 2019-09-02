# -*- coding: utf-8 -*-
"""Types module

All of the types defined in this module are specific to this package.
"""
from typing import NamedTuple


class Document(NamedTuple):
    """A document class
    """
    name: str
    content: str

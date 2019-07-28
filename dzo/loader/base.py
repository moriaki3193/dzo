# -*- coding: utf-8 -*-
"""Base class for loader classes.
"""
from abc import ABCMeta, abstractmethod
from typing import List, NamedTuple


class _Document(NamedTuple):
    """A raw document class.
    """
    name: str
    content: str


class LoaderBase(metaclass=ABCMeta):
    """A base class for loaders.

    All loaders inherit this base class should have implementations of methods
    defined in this class.
    """

    @abstractmethod
    def load(self) -> List[_Document]:
        raise NotImplementedError

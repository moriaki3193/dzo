# -*- coding: utf-8 -*-
"""Base module
"""
from abc import ABCMeta, abstractmethod
from typing import List

from .annot import Document, Token


class AbstractLoader(metaclass=ABCMeta):
    """An abstract base class for loaders.

    All loaders inherit this meta“ class should have implementations of methods
    defined in this class.
    """

    @abstractmethod
    def load(self) -> List[Document]:
        """This method returns a list of documents.
        """
        raise NotImplementedError


class AbstractTokenizer(metaclass=ABCMeta):
    """Ab abstract base class for tokenizers.

    All tokenizers inherit this meta class should have implementations of methods
    defined in this class.
    """

    name: str
    version: str

    @abstractmethod
    def tokenize(self, sentence: str) -> List[Token]:
        """Tokenize a given sentence.
        """
        raise NotImplementedError

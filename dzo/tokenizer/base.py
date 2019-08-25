# -*- coding: utf-8 -*-
"""Base classes
"""
from abc import ABCMeta, abstractmethod


class TokenBase:
    """A base class for tokens.
    """

    def get_normalized(self) -> str:
        """Returns a normalized form.
        """
        raise NotImplementedError


class TokenizerBase(metaclass=ABCMeta):
    """A base class for tokenizers.

    Attributes:
        name: tokenizer's name
        version: tokenizer's version. e.g. 'x.y.z'.
    """

    name: str
    version: str

    @abstractmethod
    def tokenize(self, sentence: str):
        """Tokenize a given sentence.
        """
        raise NotImplementedError

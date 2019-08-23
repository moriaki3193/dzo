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
    """

    @abstractmethod
    def tokenize(self, sentence: str):
        """Tokenize a given sentence.
        """
        raise NotImplementedError

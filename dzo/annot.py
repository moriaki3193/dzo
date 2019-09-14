# -*- coding: utf-8 -*-
"""Types module

All of the types defined in this module are specific to this package.
"""
from abc import ABCMeta, abstractmethod
from typing import List, NamedTuple, TypeVar


Loader = TypeVar('Loader', bound='AbstractLoader')
Token = TypeVar('Token', bound='AbstractToken')
Tokenizer = TypeVar('Tokenizer', bound='AbstractTokenizer')


class Document(NamedTuple):
    """A document class
    """
    name: str
    content: str


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


class AbstractToken(metaclass=ABCMeta):
    """An abstract base class for tokens.

    All tokens inherit this base meta should have implementations of methods
    defined in this class.
    """

    @abstractmethod
    @property
    def normalized(self) -> str:
        """Returns a normalized form.
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

# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring, no-self-use, unused-argument
"""Types module

All of the types defined in this module are specific to this package.
"""
from typing import List, NamedTuple
from typing_extensions import Protocol


class Document(NamedTuple):
    """A document class
    """
    name: str
    content: str


class Loader(Protocol):

    def load(self) -> List[Document]:
        ...


class Token(Protocol):

    @property
    def normalized(self) -> str:
        ...


class Tokenizer(Protocol):

    name: str
    version: str

    def tokenize(self, sentence: str) -> List[Token]:
        ...

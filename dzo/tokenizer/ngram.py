# -*- coding: utf-8 -*-
"""N-gram tokenizer module
"""
from typing import List, NamedTuple, cast

from ..annot import Token
from ..base import AbstractTokenizer
from ..const import _VERSION


class NGramToken(NamedTuple):
    """Result schema for NGramTokenizer().tokeinze instance method.
    """

    surface: str

    @property
    def normalized(self) -> str:  # pylint: disable=missing-docstring
        return self.surface


class NGramTokenizer(AbstractTokenizer):
    """N-gram tokenizer.
    """

    name: str = 'NGramTokenizer'
    version: str = _VERSION

    def __init__(self, n: int = 3) -> None:
        self.n = n

    def tokenize(self, sentence: str) -> List[Token]:
        """N-gram tokenization.

        Example:
            >>> tokenizer = NGramTokenizer(n=3)
            >>> sentence = 'hello'
            >>> [t.normalized for t in tokenizer.tokenize(sentence)]
            ['hel', 'ell', 'llo']

        Args:
            sentence: a sentence to be tokenized.

        Returns:
            a list of tokens.
        """
        if len(sentence) < self.n:
            return [cast(Token, NGramToken(sentence))]
        l = len(sentence)
        return [cast(Token, NGramToken(sentence[i:i+self.n])) for i in range(l-self.n+1)]

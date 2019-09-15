# -*- coding: utf-8 -*-
"""Whitespace tokenizer module.
"""
import re
from typing import NamedTuple, List, cast

from ..annot import Token
from ..base import AbstractTokenizer
from ..const import _VERSION


class WhitespaceToken(NamedTuple):
    """Result schema for WhitespaceTokenizer().tokenize instance method.
    """

    surface: str

    @property
    def normalized(self) -> str:  # pylint: disable=missing-docstring
        return self.surface


class WhitespaceTokenizer(AbstractTokenizer):
    """Whitespace tokenizer.
    """

    name: str = 'WhitespaceTokenizer'
    version: str = _VERSION

    def __init__(self) -> None:
        pass

    @staticmethod
    def tokenize(sentence: str) -> List[Token]:
        """Tokenization by splitting sentence by whitespaces simply.

        Example:
            >>> tokenizer = WhitespaceTokenizer()
            >>> sentence = 'super hyper ultra miracle romantic sentence'
            >>> [t.normalized for t in tokenizer.tokenize(sentence)]
            ['super', 'hyper', 'miracle', 'romantic', 'sentence']

        Args:
            sentence: a sentence to be tokenized.

        Returns:
            a list of tokens.
        """
        res = re.split(r'\s+', sentence)
        return [cast(Token, WhitespaceToken(tok)) for tok in res if tok]

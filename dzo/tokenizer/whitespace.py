# -*- coding: utf-8 -*-
"""Whitespace tokenizer module.
"""
import re
from typing import List

from .base import TokenizerBase
from .token import WhitespaceToken
from .._meta import _VERSION


WhitespaceTokens = List[WhitespaceToken]


class WhitespaceTokenizer(TokenizerBase):
    """Whitespace tokenizer.
    """

    name: str = 'WhitespaceTokenizer'
    version: str = _VERSION

    def __init__(self) -> None:
        pass

    def tokenize(self, sentence: str) -> WhitespaceTokens:
        """Tokenization by splitting sentence by whitespaces simply.

        Example:
            >>> tokenizer = WhitespaceTokenizer()
            >>> s = 'super hyper ultra miracle romantic sentence'
            >>> tokenizer.tokenize(s)
            ['super', 'hyper', 'miracle', 'romantic', 'sentence']

        Args:
            sentence: a sentence to be tokenized.

        Returns:
            a list of tokens.
        """
        res = re.split(r'\s+', sentence)
        return [WhitespaceToken(tok) for tok in res if tok]

# -*- coding: utf-8 -*-
"""N-gram tokenizer module
"""
from .base import TokenizerBase
from .token import NGramToken
from .types import NGramTokens
from .._meta import __VERSION


class NGramTokenizer(TokenizerBase):
    """N-gram tokenizer.
    """

    name: str = 'NGramTokenizer'
    version: str = __VERSION

    def __init__(self, n: int = 3) -> None:
        self.n = n

    def tokenize(self, sentence: str) -> NGramTokens:
        """N-gram tokenization.
        """
        if len(sentence) < self.n:
            return [NGramToken(sentence)]
        return [NGramToken(sentence[i:i+self.n]) for i in range(len(sentence)-self.n+1)]

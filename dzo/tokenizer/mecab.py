# -*- coding: utf-8 -*-
"""MeCab tokenizer module
"""
from typing import List, NamedTuple, Tuple

import MeCab

from ..annot import Token
from ..base import AbstractTokenizer
from ..const import _VERSION


class MeCabToken(NamedTuple):
    """Result schema for MeCabTokenizer().tokenize instance method.
    """

    surface: str
    pos: Tuple[str, ...]
    infl_type: str
    infl_form: str
    base_form: str
    reading: str
    phonetic: str

    @property
    def normalized(self) -> str:  # pylint: disable=missing-docstring
        return self.base_form


class MeCabTokenizer(AbstractTokenizer):
    """MeCab tokenizer.
    """

    name: str = 'MeCabTokenizer'
    version: str = _VERSION

    def __init__(self, tagger: MeCab.Tagger) -> None:
        self.tagger = tagger

    def tokenize(self, sentence: str) -> List[Token]:
        """MeCab morphological analysis tokenization.

        Example:
            >>> d = '/path/to/dicdir'
            >>> tagger = MeCab.Tagger(d)  # import MeCab package in advance
            >>> tokenizer = MeCabTokenizer(tagger)
            >>> sentence = '隣の客はよく柿食う客だ'
            >>> [t.normalized for t in tokenizer.tokenize(sentence)]
            ['隣', 'の', '客', 'は', 'よく', '柿', '食う', '客', 'だ']

        Args:
            sentence: a sentence to be tokenized.

        Returns:
            a list of tokens.
        """
        self.tagger.parse('')
        node = self.tagger.parseToNode(sentence)
        tokens: List[Token] = []
        while node:
            if node.surface:
                surface = node.surface
                features = node.feature.split(',')
                if len(features) < 9:
                    pad_size = 9 - len(features)
                    features += ['*'] * pad_size
                token = MeCabToken(
                    surface,
                    tuple(','.join(features[:4])),
                    features[4],
                    features[5],
                    features[6],
                    features[7],
                    features[8],
                )
                tokens.append(token)
            node = node.next
        return tokens

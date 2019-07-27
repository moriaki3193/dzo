# -*- coding: utf-8 -*-
"""MeCab tokenizer module
"""
import MeCab

from .base import TokenizerBase
from .token import MeCabToken
from .types import MeCabTokens


class MeCabTokenizer(TokenizerBase):
    """MeCab tokenizer.
    """

    def __init__(self, tagger: MeCab.Tagger) -> None:
        self.tagger = tagger

    def tokenize(self, sentence: str) -> MeCabTokens:
        """MeCab morphological analysis tokenization.
        """
        self.tagger.parse('')
        node = self.tagger.parseToNode(sentence)
        tokens: MeCabTokens = []
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

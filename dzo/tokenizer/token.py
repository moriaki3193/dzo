# -*- coding: utf-8 -*-
"""Token schema module.
"""
from typing import NamedTuple, Tuple


# TODO make token classes have interface `get_normalized()`.
class NGramToken(NamedTuple):
    """Result schema for NGramTokenizer.tokeinze method.
    """
    surface: str

    def get_normalized(self) -> str:  # pylint: disable=missing-docstring
        return self.surface


class MeCabToken(NamedTuple):
    """Result schema for MeCabTokenizer.tokenize method.
    """
    surface: str
    pos: Tuple[str, ...]
    infl_type: str
    infl_form: str
    base_form: str
    reading: str
    phonetic: str

    def get_normalized(self) -> str:  # pylint: disable=missing-docstring
        return self.base_form

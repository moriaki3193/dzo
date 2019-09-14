# -*- coding: utf-8 -*-
# TODO setup MeCab enabled environment in CircleCI.
"""Testing mecab module.
"""
# from dzo.tokenizer import MeCabTokenizer
from dzo.tokenizer.mecab import MeCabToken


def test_MeCabToken() -> None:
    """Test for MeCabToken.
    """
    token = MeCabToken('a', 'b', 'c', 'd', 'e', 'f', 'g')

    assert hasattr(token, 'surface')
    assert hasattr(token, 'pos')
    assert hasattr(token, 'infl_type')
    assert hasattr(token, 'infl_form')
    assert hasattr(token, 'base_form')
    assert hasattr(token, 'reading')
    assert hasattr(token, 'phonetic')

    assert token.normalized == 'e'

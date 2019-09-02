# -*- coding: utf-8 -*-
"""Testing token module.
"""
from dzo.tokenizer.token import MeCabToken, NGramToken, WhitespaceToken


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

    assert token.get_normalized() == 'e'


def test_NGramToken() -> None:
    """Test for NGramToken.
    """
    token = NGramToken('a')

    assert hasattr(token, 'surface')

    assert token.get_normalized() == 'a'


def test_WhitespaceToken() -> None:
    """Test for WhitespaceToken.
    """
    token = WhitespaceToken('a')

    assert hasattr(token, 'surface')

    assert token.get_normalized() == 'a'

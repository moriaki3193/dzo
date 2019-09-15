# -*- coding: utf-8 -*-
"""Testing whitespace module.
"""
from dzo.tokenizer import WhitespaceTokenizer
from dzo.tokenizer.whitespace import WhitespaceToken


def test_WhitespaceToken() -> None:
    """Test for WhitespaceToken.
    """
    token = WhitespaceToken('a')

    assert hasattr(token, 'surface')

    assert token.normalized == 'a'


def test_WhitespaceTokenizer_tokenize() -> None:
    """Test for tokenizer.WhitespaceTokenizer().tokenize method.
    """
    sentence = 'super ultra  hyper    miracle　romantic sentence'  # contains full-width space
    res = WhitespaceTokenizer().tokenize(sentence)
    got = [tok.normalized for tok in res]
    want = ['super', 'ultra', 'hyper', 'miracle', 'romantic', 'sentence']
    assert isinstance(res, list)
    assert isinstance(res[0], WhitespaceToken)
    assert got == want

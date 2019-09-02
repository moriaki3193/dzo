# -*- coding: utf-8 -*-
"""Testing whitespace module.
"""
from dzo.tokenizer import WhitespaceTokenizer
from dzo.tokenizer.token import WhitespaceToken


def test_WhitespaceTokenizer_tokenize() -> None:
    """Test for tokenizer.WhitespaceTokenizer().tokenize method.
    """
    sentence = 'super ultra  hyper    miracle　romantic sentence'  # contains full-width space
    res = WhitespaceTokenizer().tokenize(sentence)
    got = [tok.get_normalized() for tok in res]
    want = ['super', 'ultra', 'hyper', 'miracle', 'romantic', 'sentence']
    assert isinstance(res, list)
    assert isinstance(res[0], WhitespaceToken)
    assert got == want

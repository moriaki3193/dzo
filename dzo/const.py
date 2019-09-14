# -*- coding: utf-8 -*-
"""Constant module
"""
import logging

from .utility import read_pkg_version


DEFAULT_LOG_LEVEL: int = logging.DEBUG
_VERSION: str = read_pkg_version()

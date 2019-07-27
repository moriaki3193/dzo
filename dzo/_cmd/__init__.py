# -*- coding: utf-8 -*-
"""cmd package initialization script.
"""
from enum import Enum


class ExitStatus(Enum):
    """Program exit code constatns.
    """
    SUCCESS = 0
    ERROR = 1
    ERROR_INVALID_USAGE = 2
    ERROR_NOT_EXECUTABLE = 126
    ERROR_CTRL_C = 130

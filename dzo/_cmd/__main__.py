# -*- coding: utf-8 -*-
"""The main entry point.

Invoke as `dzo` or `python3 -m dzo`.
"""
from argparse import ArgumentParser

from . import ExitStatus
from .preprocess import preprocess
from .search import search


# Create the top-level parser
parser = ArgumentParser(prog='dzo')
subparsers = parser.add_subparsers(title='subcommands', description='search')

# Create the parser for the "preprocess" command
parser_preprocess = subparsers.add_parser(
    'preprocess',
    help='preprocess <dir> [--output /path/to/output]')
parser_preprocess.add_argument('target_dir', type=str, help='search target directory')
parser_preprocess.add_argument('result_path', type=str, help='a path to preprocess result')
parser_preprocess.add_argument('--ignore', nargs='+', help='file extensions to be ignored')
parser_preprocess.set_defaults(handler=preprocess)

# Create the parser for the "search" command
parser_search = subparsers.add_parser(
    'search',
    help='search <query> [--index-path /path/to/resource]')
parser_search.add_argument('query', type=str, help='search query')
parser_search.add_argument(
    '--index-path',
    '-i',
    type=str,
    help='a path to inverted index',
    required=True)
parser_search.set_defaults(handler=search)


def main() -> None:
    """Command line application.
    """
    try:
        cmdargs = parser.parse_args()
        if hasattr(cmdargs, 'handler'):
            status: ExitStatus = cmdargs.handler(cmdargs)
            parser.exit(status.value)
        else:
            parser.print_usage()
    except KeyboardInterrupt:
        parser.exit(status=ExitStatus.ERROR_CTRL_C.value)


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
"""dzo package setup script.
"""
from os import path
from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

import dzo


# License
with open(path.join(path.dirname(path.abspath(__file__)), 'LICENSE')) as fp:
    LICENSE = fp.read().strip('\n')

# Literal
NAME = 'dzo'
AUTHOR = 'Moriaki Saigusa'
AUTHOR_EMAIL = 'moriaki3193@gmail.com'
LONG_DESCRIPTION = 'Python implemented portable and easy-to-use search engine'
URL = 'https://github.com/moriaki3193/dzo'
KEYWORDS = 'Python Search Engine'
TEST_SUITE = 'tests'
ZIP_SAFE = False

# List
PACKAGES = find_packages(exclude=('tests'))
TESTS_REQUIRE = ['pytest', 'pytest-cov']
SETUP_REQUIRES = ['pytest-runner']
INSTALL_REQUIRES = ['Cython', 'numpy', 'scipy', 'mecab-python3']
CLASSIFIERS = [
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
]

# Dict
ENTRY_POINTS = {
    'console_scripts': [
        'dzo=dzo._cmd.__main__:main'
    ]
}
EXTRAS_REQUIRE = {
    'dev': ['mypy', 'pylint', 'numpy-stubs']
}

# Commands
CMDCLASS = {'build_ext': build_ext}

# Cython extensions
EXT_DIR = path.join(path.dirname(path.abspath(__file__)), 'dzo', '_ext')
EXT_MODULES = [
    Extension('dzo._ext.core', [path.join(EXT_DIR, 'core.pyx')]),
]


setup(
    name=NAME,
    version=dzo.__version__,
    description=dzo.__doc__.strip(),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    packages=PACKAGES,
    tests_require=TESTS_REQUIRE,
    extras_require=EXTRAS_REQUIRE,
    setup_requires=SETUP_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    entry_points=ENTRY_POINTS,
    cmdclass=CMDCLASS,
    test_suite=TEST_SUITE,
    zip_safe=ZIP_SAFE,
    ext_modules=cythonize(EXT_MODULES, language_level='3')
)

#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""Functions for parsing module headers.

@author   Hank Adler
@version  0.1.0
@license  MIT
"""


import re
import sys


def get(fname):
    """Opens `fname` and reads its header.

    `header` is the first docstring found on `fname`.

    Parameters:
        fname (str): Path to human readable file.

    Returns:
        str: File header information.
    """
    header = ''
    try:
        with open(fname, 'r') as fh:
            match = re.findall(r'"""(.*)"""\s', fh.read(), re.DOTALL)
            if match is not None:
                header = ''.join(match).split('"""')[0].strip()
    except FileNotFoundError:
        print("ERROR: '%s' not found!" % fname, file=sys.stderr)
        return

    return header


def getAuthor(fname):
    """Gets author from header.

    Author is assumed to be specified with @author tag in header.

    Parameters:
        fname (str): Path to human readable file.

    Returns:
        str: File author.
    """
    header = get(fname)
    match = re.findall(r'[Aa]uthor\s+(.*)', header)
    if match:
        return match[0]


def getVersion(fname):
    """Gets file version from header.

    Parameters:
        fname (str): Path to human readable file.

    Returns:
        str: file version.
    """
    header = get(fname)
    match = re.findall(r'[Vv]ersion\s+(.*)', header)
    if match:
        return match[0]


if __name__ == '__main__':
    pass

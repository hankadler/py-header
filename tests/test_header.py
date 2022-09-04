#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""Unit tests for header module.

@author   Hank Adler
@version  0.1.0
@license  MIT
"""


import datetime
import os
import textwrap
import unittest

import logger
from src import header


class Test(unittest.TestCase):
    """Tests all header functions."""

    result = unittest.TestResult()
    name = 'header'
    # WARNING: the following relies on header.get_version(); one of the
    # functions tested here. Hence the catchall try-except construct.
    try:
        version = header.getVersion(
            ''.join(header.__path__) + '/' + name + '.py'
        )
    except:
        version = '6.6.6'
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    log = logger.get(__name__, '%s-%s-unittest-%s' % (name, version, date))

    # Override
    def setUp(self):
        self.dummy_header = textwrap.dedent('''\
            """
            dummy.py
                A dummy header.

            @author   John Smith
            @version  7.7.7
            """
        ''')
        with open('dummy.py', 'w') as fh:
            fh.write(self.dummy_header)

    # Override
    def tearDown(self):
        os.remove('dummy.py')

    def _logResult(self):
        """Logs most recent result."""
        if self.result.wasSuccessful():
            self.log.info('RESULT: PASS')
        else:
            self.log.info('RESULT: FAIL')
        self.log.info('%s' % '-' * 63)

    def testGet(self):
        self.log.info("  TEST: header.get('dummy.py')")
        self.assertEqual(
            header.get('dummy.py').strip(),
            self.dummy_header.replace('"""', '').strip(),
        )
        self._logResult()

    def testGetVersion(self):
        self.log.info("  TEST: header.get_version('dummy.py')")
        self.log.debug(f"version = {header.getVersion('dummy.py')}")
        self.assertEqual(header.getVersion('dummy.py'), '7.7.7')
        self._logResult()

    def testGetAuthor(self):
        self.log.info("  TEST: header.get_author('dummy.py')")
        self.assertEqual(header.getAuthor('dummy.py'), 'John Smith')
        self._logResult()


if __name__ == '__main__':
    unittest.main()

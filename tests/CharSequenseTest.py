__author__ = 'WWW'
import unittest
class CharSequenseTest(unittest.TestCase):

    def test_upper(self):
          self.assertEqual('foo'.upper(), 'FOO')
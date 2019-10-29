import unittest
from production.roman_numerals import RomanNumeral


class TestConvert(unittest.TestCase):
    def test_zero_is_empty_string(self):
        self.assertEqual('', str(RomanNumeral(0)))

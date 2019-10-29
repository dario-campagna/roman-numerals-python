import unittest
from production.roman_numerals import RomanNumeral


class TestConvert(unittest.TestCase):
    def test_0_is_empty_string(self):
        self.assertEqual('', str(RomanNumeral(0)))

    def test_1_is_I(self):
        self.assertEqual('I', str(RomanNumeral(1)))

import unittest
from production.roman_numerals import RomanNumeral


class TestConvert(unittest.TestCase):
    def test_0_is_empty_string(self):
        self.assertEqual('', str(RomanNumeral(0)))

    def test_1_is_I(self):
        self.assertEqual('I', str(RomanNumeral(1)))

    def test_2_is_II(self):
        self.assertEqual('II', str(RomanNumeral(2)))

    def test_3_is_III(self):
        self.assertEqual('III', str(RomanNumeral(3)))
    
    def test_4_is_IV(self):
        self.assertEqual('IV', str(RomanNumeral(4)))
    
    def test_5_is_V(self):
        self.assertEqual('V', str(RomanNumeral(5)))
    
    def test_6_is_VI(self):
        self.assertEqual('VI', str(RomanNumeral(6)))
    
    def test_7_is_VII(self):
        self.assertEqual('VII', str(RomanNumeral(7)))
    
    def test_9_is_IX(self):
        self.assertEqual('IX', str(RomanNumeral(9)))

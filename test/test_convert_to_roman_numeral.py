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

    def test_10_is_X(self):
        self.assertEqual('X', str(RomanNumeral(10)))

    def test_18_is_XVIII(self):
        self.assertEqual('XVIII', str(RomanNumeral(18)))

    def test_50_is_L(self):
        self.assertEqual('L', str(RomanNumeral(50)))

    def test_60_is_LX(self):
        self.assertEqual('LX', str(RomanNumeral(60)))

    def test_40_is_XL(self):
        self.assertEqual('XL', str(RomanNumeral(40)))

    def test_100_is_C(self):
        self.assertEqual('C', str(RomanNumeral(100)))

    def test_90_is_XC(self):
        self.assertEqual('XC', str(RomanNumeral(90)))

    def test_500_is_D(self):
        self.assertEqual('D', str(RomanNumeral(500)))

    def test_400_is_CD(self):
        self.assertEqual('CD', str(RomanNumeral(400)))

    def test_1000_is_M(self):
        self.assertEqual('M', str(RomanNumeral(1000)))

    def test_900_is_CM(self):
        self.assertEqual('CM', str(RomanNumeral(900)))

    def test_1776_is_MDCCLXXVI(self):
        self.assertEqual('MDCCLXXVI', str(RomanNumeral(1776)))

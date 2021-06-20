import unittest
from roman import RomanConverter

class test(unittest.TestCase):

    def test_rom_calculate(self):
        c = RomanConverter()
        self.assertEqual(c.convert("MCMXLIV"),1944)

    def test_rom_valid(self):
        c = RomanConverter()
        self.assertEqual(c.convert("MMCXXIK"),"Invalid number")

    def test_to_roman_convert(self):
        c = RomanConverter()
        self.assertEqual(c.to_roman_convert(2330),"MMCCCXXX")

    def test_to_roman_zero(self):
        c = RomanConverter()
        with self.assertRaises(ValueError) as context:
            c.to_roman_convert(0)
            self.assertTrue('Invalid number' in context.exception)

    def test_to_roman_negative(self):
        c = RomanConverter()
        with self.assertRaises(ValueError) as context:
            c.to_roman_convert(-2)
            self.assertTrue('Invalid number' in context.exception)

    def test_to_roman_non_integer(self):
        c = RomanConverter()
        with self.assertRaises(ValueError) as context:
            c.to_roman_convert(120.5)
            self.assertTrue('Invalid number' in context.exception)



if __name__ == '__main__':
    unittest.main()



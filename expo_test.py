import unittest
from expo import expo


class ExpoTest(unittest.TestCase):
    def test_both_positive(self):
        result = expo(2, 2)
        self.assertEqual(result, 4)

    def test_positive_to_negative(self):
        result = expo(2, -2)
        self.assertEqual(result, 0.25)

    def test_negative_to_positive(self):
        result = expo(-2, 2)
        self.assertEqual(result, -4)

    def test_both_negative(self):
        result = expo(-2, -2)
        self.assertEqual(result, -0.25)

    def test_base_to_zero(self):
        result = expo(2, 0)
        self.assertEqual(result, 1)

    def test_zero_to_power(self):
        result = expo(0, 2)
        self.assertEqual(result, 0)

    def test_both_zero(self):
        with self.assertRaises(ArithmeticError):
            expo(0, 0)


if __name__ == "__main__":
    unittest.main()

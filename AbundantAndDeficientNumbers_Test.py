import unittest
from AbundeficientNumbers import AbundeficientCalculator

class AbundeficientNumbers_Test(unittest.TestCase):
    def test_IsAbundant(self):
        self.assertTrue(AbundeficientCalculator.is_abundant(220))
        self.assertTrue(AbundeficientCalculator.is_abundant(112))
        self.assertTrue(AbundeficientCalculator.is_abundant(12))

    def test_IsDeficient(self):
        self.assertTrue(AbundeficientCalculator.is_deficient(69))
        self.assertTrue(AbundeficientCalculator.is_deficient(85))
        self.assertTrue(AbundeficientCalculator.is_deficient(134))

    def test_IsNeither(self):
        self.assertTrue(AbundeficientCalculator.is_neither(6))
        self.assertTrue(AbundeficientCalculator.is_neither(28))
        self.assertTrue(AbundeficientCalculator.is_neither(496))

    def test_abundantCalculation(self):
        self.assertEqual(64, AbundeficientCalculator.get_result(220))
        self.assertEqual(24, AbundeficientCalculator.get_result(112))
        self.assertEqual(4, AbundeficientCalculator.get_result(12))

    def test_deficientCalculation(self):
        self.assertEqual(64, AbundeficientCalculator.get_result(220))
        self.assertEqual(24, AbundeficientCalculator.get_result(112))
        self.assertEqual(4, AbundeficientCalculator.get_result(12))

    def test_get_proper_divisors(self):
        self.assertEqual([], AbundeficientCalculator.get_proper_divisors(0))
        self.assertEqual([], AbundeficientCalculator.get_proper_divisors(1))
        self.assertEqual([1], AbundeficientCalculator.get_proper_divisors(2))
        self.assertEqual([1], AbundeficientCalculator.get_proper_divisors(3))
        self.assertEqual([1, 2], AbundeficientCalculator.get_proper_divisors(4))
        self.assertEqual([1], AbundeficientCalculator.get_proper_divisors(5))
        self.assertEqual([1, 2, 3], AbundeficientCalculator.get_proper_divisors(6))
        self.assertEqual([1, ], AbundeficientCalculator.get_proper_divisors(7))
        self.assertEqual([1, 2, 4], AbundeficientCalculator.get_proper_divisors(8))
        self.assertEqual([1, 3], AbundeficientCalculator.get_proper_divisors(9))

if __name__ == '__main__':
    unittest.main()

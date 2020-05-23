import unittest
from challenge228_AlphabeticalOrder.AlphabeticalOrder import AlphabeticalOrderizer

class AlphabeticalOrder_Test(unittest.TestCase):
    def test_is_alphabetical(self):
        self.assertTrue(AlphabeticalOrderizer.IsAlphabeticalOrder('billowy'))
        self.assertTrue(AlphabeticalOrderizer.IsAlphabeticalOrder('biopsy'))
        self.assertTrue(AlphabeticalOrderizer.IsAlphabeticalOrder('chinos'))
        self.assertTrue(AlphabeticalOrderizer.IsAlphabeticalOrder('chintz'))
        self.assertTrue(AlphabeticalOrderizer.IsAlphabeticalOrder('bijoux'))
        self.assertTrue(AlphabeticalOrderizer.IsAlphabeticalOrder('abhors'))
        self.assertTrue(AlphabeticalOrderizer.IsAlphabeticalOrder('begins'))
        self.assertTrue(AlphabeticalOrderizer.IsAlphabeticalOrder('chimps'))

    def test_is_not_alphabetical(self):
        self.assertFalse(AlphabeticalOrderizer.IsAlphabeticalOrder('defaced'))
        self.assertFalse(AlphabeticalOrderizer.IsAlphabeticalOrder('fiddle'))

    def test_is_reverse_alphatical(self):
        self.assertTrue(AlphabeticalOrderizer.IsReverseAlphabeticalOrder('sponged'))
        self.assertTrue(AlphabeticalOrderizer.IsReverseAlphabeticalOrder('wronged'))

if __name__ == '__main__':
    unittest.main()

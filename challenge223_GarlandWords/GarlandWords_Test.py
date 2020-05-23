import unittest
import GarlandWords

class GarlandWords_Test(unittest.TestCase):

    def test_DegreeZero(self):
        self.assertEqual(0, GarlandWords.GarlandWords("programmer"))

    def test_DegreeOne(self):
        self.assertEqual(1, GarlandWords.GarlandWords("ceramic"))

    def test_DegreeTwo(self):
        self.assertEqual(2, GarlandWords.GarlandWords("onion"))

    def test_DegreeFour(self):
        self.assertEqual(4, GarlandWords.GarlandWords("alfalfa"))

    def test_DegreeFive(self):
        self.assertEqual(5, GarlandWords.GarlandWords("undergrounder"))
        self.assertEqual(5, GarlandWords.GarlandWords("alangalang"))

    def test_DegreeNine(self):
        self.assertEqual(9, GarlandWords.GarlandWords("kailangang-kailangan"))

if __name__ == '__main__':
    unittest.main()

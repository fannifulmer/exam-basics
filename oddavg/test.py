import unittest
import odd_avg

class TestOddAvg(unittest.TestCase):
    def test_odd_average(self):
        self.assertEqual(odd_avg.odd_average([2, 3, 4, 5, 6]), 4)
    def test_odd_average_empthy(self):
        self.assertEqual(odd_avg.odd_average([]), None)
    def test_odd_average_even(self):
        self.assertEqual(odd_avg.odd_average([2, 4, 6, 8]), None)

if __name__ == '__main__':
    unittest.main()
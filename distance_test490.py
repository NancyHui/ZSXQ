import unittest
from distance490 import distance_from_zero


class test(unittest.TestCase):
    def test_int(self):
        self.assertEqual(100, distance_from_zero(-100))

    def test_float(self):
        self.assertEqual(100.1, distance_from_zero(-100.1))

    def test_string(self):
        self.assertEqual("Error: Can not be calculated!", distance_from_zero("Hello world!"))

    def test_list(self):
        self.assertEqual("Error: Can not be calculated!", distance_from_zero({-100}))


if __name__ == '__main__':
    unittest.main(verbosity=2)


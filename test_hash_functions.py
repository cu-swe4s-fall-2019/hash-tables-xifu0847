import unittest
import hash_functions


class TestHashFunction(unittest.TestCase):
    '''
    Unit test for hash_function.py
    '''
    def test_h_ascii(self):
        self.assertEqual(hash_functions.h_ascii('test', 1000), 448)
        self.assertNotEqual(
            hash_functions.h_ascii('test', 1000),
            hash_functions.h_ascii('abcd', 1000))
        self.assertEqual(
            hash_functions.h_ascii('test', 1000),
            hash_functions.h_ascii('estt', 1000))

    def test_h_rolling(self):
        # The ground truth are calculated manually
        self.assertEqual(hash_functions.h_rolling('test', 1000), 652)
        self.assertEqual(hash_functions.h_rolling('estt', 1000), 876)

    def test_h_DJB(self):
        # The ground truth are calculated manually
        self.assertEqual(hash_functions.h_DJB('test', 1000), 493)
        self.assertEqual(hash_functions.h_DJB('estt', 1000), 717)


if __name__ == '__main__':
    unittest.main()

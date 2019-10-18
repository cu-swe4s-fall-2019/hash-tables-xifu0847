import unittest
import os
import hash_tables
import hash_functions


class TestHashTables(unittest.TestCase):

    def test_linear_probing(self):
        ascii_test = hash_tables.LinearProbe(1000, hash_functions.h_ascii)
        ascii_test.add('test_key', 'test_value')
        self.assertEqual(ascii_test.search('test_key'), 'test_value')
        self.assertNotEqual(ascii_test.search('test_key'), 'bad')
        self.assertEqual(ascii_test.search('bad_key'), None)

        rolling_test = hash_tables.LinearProbe(1000, hash_functions.h_rolling)
        rolling_test.add('test_key', 'test_value')
        self.assertEqual(rolling_test.search('test_key'), 'test_value')
        self.assertNotEqual(rolling_test.search('test_key'), 'bad')
        self.assertEqual(rolling_test.search('bad_key'), None)

        DJB_test = hash_tables.LinearProbe(1000, hash_functions.h_DJB)
        DJB_test.add('test_key', 'test_value')
        self.assertEqual(DJB_test.search('test_key'), 'test_value')
        self.assertNotEqual(DJB_test.search('test_key'), 'bad')
        self.assertEqual(DJB_test.search('bad_key'), None)

    def test_chained_hash(self):
        ascii_test = hash_tables.ChainedHash(1000, hash_functions.h_ascii)
        ascii_test.add('test_key', 'test_value')
        self.assertEqual(ascii_test.search('test_key'), 'test_value')
        self.assertNotEqual(ascii_test.search('test_key'), 'bad')
        self.assertEqual(ascii_test.search('bad_key'), None)

        rolling_test = hash_tables.ChainedHash(1000, hash_functions.h_rolling)
        rolling_test.add('test_key', 'test_value')
        self.assertEqual(rolling_test.search('test_key'), 'test_value')
        self.assertNotEqual(rolling_test.search('test_key'), 'bad')
        self.assertEqual(rolling_test.search('bad_key'), None)

        DJB_test = hash_tables.ChainedHash(1000, hash_functions.h_DJB)
        DJB_test.add('test_key', 'test_value')
        self.assertEqual(DJB_test.search('test_key'), 'test_value')
        self.assertNotEqual(DJB_test.search('test_key'), 'bad')
        self.assertEqual(DJB_test.search('bad_key'), None)

    def test_pseudo_random_hash(self):
        ascii_test = hash_tables.PseudoRandomHash(1000, hash_functions.h_ascii)
        ascii_test.add('test_key', 'test_value')
        self.assertEqual(ascii_test.search('test_key'), 'test_value')
        self.assertNotEqual(ascii_test.search('test_key'), 'bad')
        self.assertEqual(ascii_test.search('bad_key'), None)

        rolling_test = hash_tables.PseudoRandomHash(
            1000, hash_functions.h_rolling)
        rolling_test.add('test_key', 'test_value')
        self.assertEqual(rolling_test.search('test_key'), 'test_value')
        self.assertNotEqual(rolling_test.search('test_key'), 'bad')
        self.assertEqual(rolling_test.search('bad_key'), None)

        DJB_test = hash_tables.PseudoRandomHash(1000, hash_functions.h_DJB)
        DJB_test.add('test_key', 'test_value')
        self.assertEqual(DJB_test.search('test_key'), 'test_value')
        self.assertNotEqual(DJB_test.search('test_key'), 'bad')
        self.assertEqual(DJB_test.search('bad_key'), None)


if __name__ == '__main__':
    unittest.main()

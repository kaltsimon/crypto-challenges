"""Unittests for crypto challenges set 2."""

import unittest
import fixed_xor


class TestChallenges(unittest.TestCase):

    """Test if the challenges were correctly implemented."""

    def test_challenge_2(self):
        """Test `fixed_xor()`."""
        a = '1c0111001f010100061a024b53535009181c'
        b = '686974207468652062756c6c277320657965'
        result = fixed_xor.xor_hex(a, b)
        expected = '746865206b696420646f6e277420706c6179'
        self.assertEqual(expected, result, 'Challenge 2 failed')


if __name__ == '__main__':
    unittest.main()

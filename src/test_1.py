"""Unittests for crypto challenges set 1."""

import unittest
import encode_decode as set_1


class TestChallenges(unittest.TestCase):

    """Test if the challenges were correctly implemented."""

    def test_decode_hex(self):
        """Test decoding of hex string."""
        self.assertEqual(255, list(set_1.decode_hex('ff'))[0])
        self.assertEqual(171, list(set_1.decode_hex('ab'))[0])
        self.assertEqual(5, list(set_1.decode_hex('5'))[0])
        self.assertEqual(15, list(set_1.decode_hex('f'))[0])
        self.assertEqual([73, 39], list(set_1.decode_hex('4927')))
        self.assertEqual([15, 59, 172], list(set_1.decode_hex('0F3BAC')))
        self.assertEqual([202, 254, 186, 190],
                         list(set_1.decode_hex('CAFEBABE')))

    def test_bytes_to_int(self):
        """Test bytes -> int."""
        self.assertEqual(0, set_1.bytes_to_int(b'\x00'))
        self.assertEqual(10, set_1.bytes_to_int(b'\x0a'))
        self.assertEqual(255, set_1.bytes_to_int(b'\xff'))
        self.assertEqual(256, set_1.bytes_to_int(b'\x01\x00'))
        self.assertEqual(265, set_1.bytes_to_int(b'\x01\x09'))
        self.assertEqual(1376010, set_1.bytes_to_int(b'\x14\xff\x0a'))
        self.assertEqual(2335, set_1.bytes_to_int(b'\x00\x09\x1f'))

    def test_base64_map(self):
        """Test mapping of values to base64."""
        self.assertEqual('A', set_1.base64_map(0))
        self.assertEqual('J', set_1.base64_map(9))
        self.assertEqual('f', set_1.base64_map(31))
        self.assertEqual('3', set_1.base64_map(55))
        self.assertEqual('+', set_1.base64_map(62))
        self.assertEqual('/', set_1.base64_map(63))

    def test_int_to_base64(self):
        """Test mapping of values from int to base64."""
        self.assertEqual('AAAA', set_1.int_to_base64(0))
        self.assertEqual('AAAJ', set_1.int_to_base64(9))
        self.assertEqual('AAKf', set_1.int_to_base64(64 * 10 + 31))
        self.assertEqual('A/b/', set_1.int_to_base64((64 * 63 + 27) * 64 + 63))

    def test_encode_base64(self):
        """Test encoding of byte array to base64."""
        self.assertEqual('AJc=', set_1.encode_base64(b'\x00\x97'))

    def test_challenge_1(self):
        """Test `hex2base64()`."""
        self.assertEqual('SSc=', set_1.hex2base64('4927'))
        self.assertEqual('Dzus', set_1.hex2base64('0F3BAC'))
        self.assertEqual('DzusE0Y=', set_1.hex2base64('0F3BAC1346'))
        self.assertEqual('yv66vg==', set_1.hex2base64('CAFEBABE'))
        expected = ('SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsa'
                    + 'WtlIGEgcG9pc29ub3VzIG11c2hyb29t')
        result = set_1.hex2base64('49276d206b696c6c696e67207'
                                  + '96f757220627261696e206c6'
                                  + '96b65206120706f69736f6e6f7573'
                                  + '206d757368726f6f6d')
        self.assertEqual(expected, result, 'Challenge 1 failed')


if __name__ == '__main__':
    unittest.main()

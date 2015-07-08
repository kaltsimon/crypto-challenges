"""Perform fixed length XOR operations."""

from encode_decode import decode_hex, encode_hex


def xor_hex(hex_1, hex_2):
    """XOR two fixed length hex strings."""
    return encode_hex(xor(decode_hex(hex_1), decode_hex(hex_2)))


def xor(bytes_1, bytes_2):
    """XOR two bytearrays of the same length."""
    l1 = len(bytes_1)
    l2 = len(bytes_2)
    assert l1 == l2

    result = bytearray(l1)
    for i in range(l1):
        result[i] = bytes_1[i] ^ bytes_2[i]

    return result

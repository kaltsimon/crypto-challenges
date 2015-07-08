"""Crypto Challenges Set 1."""

from functools import wraps


def int_seq_to_bytes(func):
    """Wrap a function that returns an int sequence to return a bytearray."""
    @wraps(func)
    def wrapped(*args, **kwargs):
        seq = func(*args, **kwargs)
        return bytes(seq)
    return wrapped


@int_seq_to_bytes
def decode_hex(hexstring):
    """Decode a hex string into a byte sequence."""
    temp = ''
    second = False
    for c in hexstring:
        if second:
            temp += c
            second = False
            yield int(temp, 16)
        else:
            second = True
            temp = c

    # If we have 1 character left, decode it separately
    if len(temp) == 1 and second:
        yield int(temp, 16)


def encode_hex(byteseq):
    """Encode a byte sequence to a hex string."""
    result = ''
    for b in byteseq:
        result += hex(b)[2:]

    return result


def bytes_to_int(byteseq):
    """Convert a sequence of up to 4 bytes to a single integer."""
    result = 0
    for byte in byteseq:
        result = result << 8
        result += byte

    return result


def base64_map(val):
    """Map a value in the range 0 <= val < 64 to its base64 character."""
    assert val >= 0 and val < 64
    if val < 26:
        return chr(ord('A') + val)
    elif val < 52:
        return chr(ord('a') + val - 26)
    elif val < 62:
        return chr(ord('0') + val - 52)
    elif val == 62:
        return '+'
    elif val == 63:
        return '/'


def int_to_base64(val, char_count=4):
    """Convert an integer to base64 representation."""
    result = ''
    for i in range(char_count):  # TODO: Check if this makes sense
        x = val & 0x3f  # Get the last 6 bytes
        val = val >> 6  # Shift right by 6 bytes
        result = base64_map(x) + result

    return result


def encode_base64(bytearr):
    """Encode an array of bytes into a base64 string."""
    acc = []
    result = ''
    for b in bytearr:
        acc.append(b)
        if len(acc) == 3:  # accumulated 3 bytes
            result += int_to_base64(bytes_to_int(acc))
            acc.clear()

    if len(acc) > 0:  # handle last 1-2 bytes
        n = (3 - len(acc))
        val = bytes_to_int(acc) << 8 * n
        last = int_to_base64(val)[:-n] + n * '='
        result += last

    return result


def hex2base64(string):
    """Convert the given string from hexadecimal to base64 representation."""
    return encode_base64(decode_hex(string))


if __name__ == '__main__':
    # Challenge 1
    hex2base64('49276d206b696c6c696e6720796f757220627261696e206c6'
               + '96b65206120706f69736f6e6f7573206d757368726f6f6d')

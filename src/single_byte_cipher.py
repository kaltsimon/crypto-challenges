"""Decrypt a message that was XOR'd against a single character."""

from encode_decode import decode_hex
from fixed_xor import xor
import requests
from operator import itemgetter


def xor_with_char(bytes, char):
    """XOR a sequence of bytes with a single character."""
    return xor(bytes, char * len(bytes))


def analyze_text(text):
    """Analyze the given text for the frequencies of its characters."""
    # Initialize Dictionary
    frequencies = {}
    count = 0

    for c in text:
        c = c.lower()
        if c in frequencies:
            frequencies[c] += 1
        else:
            frequencies[c] = 1

        count += 1

    return {char: val / count for char, val in frequencies.items()}


def extract_wiki_text(wikipedia_title, language='en'):
    """Get the text of the given wikipedia article."""
    base_url = ('https://' + language + '.wikipedia.org/w/api.php?action=query'
                + '&prop=extracts&format=json&explaintext='
                + '&exsectionformat=plain&titles=')
    text = ''

    r = requests.get(base_url + wikipedia_title)
    if r.status_code == 200:
        pages = r.json()['query']['pages']
        for (id, page) in pages.items():
            text += page['extract']

    return text


def analyze_wiki_text(wikipedia_title, language='en'):
    """Analyze the text of the given Wikipedia article."""
    return analyze_text(extract_wiki_text(wikipedia_title, language))


def decrypt(bytes_, guess=0):
    """Decrypt a sequence of bytes."""
    wiki = analyze_wiki_text('Pineapple')
    dec = bytes_.decode('utf-8')
    freqs = analyze_text(dec)

    item2 = itemgetter(1)

    wiki = sorted(wiki.items(), key=item2, reverse=True)
    freqs = sorted(freqs.items(), key=item2, reverse=True)

    diffs = []

    for i in range(min(len(wiki), len(freqs))):
        diffs.append(abs(ord(wiki[i][0]) - ord(freqs[i][0])))

    return xor_with_char(bytes_, bytes([diffs[guess]]))


def decrypt_hex(hex_string):
    """Decrypt the hex encoded string."""
    return decrypt(decode_hex(hex_string))

if __name__ == '__main__':
    print(decrypt_hex('1b37373331363f78151b7f2b783431333d78'
                      + '397828372d363c78373e783a393b3736'))

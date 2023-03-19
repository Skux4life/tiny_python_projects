#!/usr/bin/env python3
"""
Author : mathewellis <mathewellis@localhost>
Date   : 2023-03-18
Purpose: apples and bananas
"""

import argparse
import os

VOWELS = ['a', 'e', 'i', 'o', 'u']

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='str',
                        type=str,
                        choices=VOWELS,
                        default='a')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    vowel = args.vowel
    for v in VOWELS:
        text = text.replace(v, vowel).replace(v.upper(), vowel.upper())

    print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()

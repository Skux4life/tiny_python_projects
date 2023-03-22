#!/usr/bin/env python3
"""
Author : mathewellis <mathewellis@localhost>
Date   : 2023-03-21
Purpose: ransom
"""

import argparse
import os
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='ransom',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed value',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    result = []
    random.seed(args.seed)

    for char in args.text.lower():
        result.append(choose(char))

    print(''.join(result))

# --------------------------------------------------
def choose(char):
    """Randomly choose an upper or lowercase letter to return"""

    return char.upper() if random.choice([0, 1]) else char.lower()


# --------------------------------------------------
if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Author : mathewellis <mathewellis@localhost>
Date   : 2023-03-19
Purpose: telephone
"""

import argparse
import os
import random
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random value seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percentage mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    if not 0 <= args.mutations < 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    text = args.text
    num_mutations = round(len(text) * args.mutations)
    substitution = ''.join(sorted(string.ascii_letters + string.punctuation))
    characters = list(text)

    indexes = random.sample(range(len(text)), num_mutations)

    for i in indexes:
        characters[i] = random.choice(substitution.replace(characters[i], ''))

    result = ''.join(characters)

    print(f'You said: "{text}"')
    print(f'I heard : "{result}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()

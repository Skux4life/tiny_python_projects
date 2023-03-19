#!/usr/bin/env python3
"""
Author : matthewellis
Date   : 2023-03-17
Purpose: Crows Nest baby
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crowsnest baby',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('object',
                        metavar='str',
                        help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Print out what is seen from the crowsnest"""

    args = get_args()
    word = args.object
    if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
        word = 'an ' + word
    else:
        word = 'a ' + word
    print(f'Ahoy, Captain, {word} off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Author : mathewellis <mathewellis@localhost>
Date   : 2023-03-21
Purpose: Bottles of beer
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-n',
                        '--num',
                        help='Number of bottles',
                        metavar='int',
                        type=int,
                        default=10)

    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    bottles_left = args.num
    while bottles_left > 1:
        bottles_of_beer(bottles_left)
        bottles_left -= 1
        if bottles_left == 1:
            print(f'{bottles_left} bottle of beer on the wall!\n')
        else:
            print(f'{bottles_left} bottles of beer on the wall!\n')

    bottles_of_beer(bottles_left, False)
    print('No more bottles of beer on the wall!')

def bottles_of_beer(num_of_bottles, plural=True):
    suffix = ' bottles' if plural else ' bottle'
    bottles = str(num_of_bottles) + suffix
    print(f'{bottles} of beer on the wall,')
    print(f'{bottles} of beer,')
    print('Take one down, pass it around,')


# --------------------------------------------------
if __name__ == '__main__':
    main()

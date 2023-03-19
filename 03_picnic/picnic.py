#!/usr/bin/env python3
"""
Author : matthewellis
Date   : 2023-03-17
Purpose: Display the items to be taken on a picnic
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic Game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('Items',
                        metavar='str',
                        help='Item(s) to bring',
                        nargs='+')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.Items
    num = len(items)

    result = ''

    if args.sorted:
        items.sort()

    if num == 1:
        result = items[0]
    elif num == 2:
        result = f'{items[0]} and {items[1]}'
    else:
        for i in range(num - 1):
            result += items[i] + ', '
        result += 'and ' + items[num - 1]

    print(f'You are bringing {result}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()

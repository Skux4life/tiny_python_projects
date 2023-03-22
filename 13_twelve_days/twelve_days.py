#!/usr/bin/env python3
"""
Author : mathewellis <mathewellis@localhost>
Date   : 2023-03-21
Purpose: 12 days of Christmas
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='12 days of Christmas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--number',
                        help='Number of days',
                        metavar='int',
                        type=int,
                        default=12)

    parser.add_argument('-o',
                        '--outfile',
                        help='An output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    args = parser.parse_args()

    if args.number not in range(1, 13):
        parser.error(
            f'--number "{args.number}" must be an integer between 1 and 12.')
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    verses = map(verse, range(1, args.number + 1))
    print('\n\n'.join(verses), file=args.outfile)


def verse(day):
    """Create a verse"""

    ordinal = [
        'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
        'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'
    ]

    gifts = [
        'A partridge in a pear tree.',
        'Two turtle doves,',
        'Three French hens,',
        'Four calling birds,',
        'Five gold rings,',
        'Six geese a laying,',
        'Seven swans a swimming,',
        'Eight maids a milking,',
        'Nine ladies dancing,',
        'Ten lords a leaping,',
        'Eleven pipers piping,',
        'Twelve drummers drumming,',
    ]

    lines = [
        f'On the {ordinal[day - 1]} day of Christmas,',
        'My true love gave to me,'
    ]

    lines.extend(reversed(gifts[:day]))

    if day > 1:
        lines[-1] = 'And ' + lines[-1].lower()

    return '\n'.join(lines)


# --------------------------------------------------
if __name__ == '__main__':
    main()

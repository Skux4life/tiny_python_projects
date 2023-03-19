#!/usr/bin/env python3
"""
Author : mathewellis <mathewellis@localhost>
Date   : 2023-03-18
Purpose: gashlycrumb
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='str',
                        help='Letter(s)',
                        nargs='+')

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')

    return parser.parse_args()

def create_dict(file):
    lines = {}
    for line in file:
        lines[line[0]] = line
    return lines

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file = args.file
    lines = create_dict(file)

    for letter in args.letter:
        print(lines.get(letter.upper(), f'I do not know "{letter}".\n'), end='')

# --------------------------------------------------
if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Author : matthewellis
Date   : 2023-03-17
Purpose: Howler
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input text')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Howl baby"""

    args = get_args()
    out = open(args.outfile, 'wt') if args.outfile else sys.stdout
    print(args.text.upper(), file=out)


# --------------------------------------------------
if __name__ == '__main__':
    main()

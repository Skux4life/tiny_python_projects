#!/usr/bin/env python3
"""
Author : mathewellis <mathewellis@localhost>
Date   : 2023-03-18
Purpose: word count exercise
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        nargs='*',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=[sys.stdin])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    total_lines, total_words, total_chars = 0, 0, 0
    for file in args.file:
        line_count, word_count, char_count = 0, 0, 0
        for line in file:
            line_count += 1
            word_count += len(line.split())
            char_count += len(line)
        print(f'{line_count:8}{word_count:8}{char_count:8} {file.name}')

        total_lines += line_count
        total_words += word_count
        total_chars += char_count

    if len(args.file) > 1:
        print(f'{total_lines:8}{total_words:8}{total_chars:8} total')


# --------------------------------------------------
if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Author : matthewellis
Date   : 2023-03-17
Purpose: Jump the 5 for a phone number
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main"""

    args = get_args()
    jumper = {'1':'9', '2':'8', '3':'7', '4':'6', '5':'0',
                '6':'4', '7':'3', '8':'2', '9':'1', '0':'5'}
    result = ''
    for char in args.input:
        result += jumper.get(char, char)
    print(result)


# --------------------------------------------------
if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='read a line from a file.')
parser.add_argument('file_name', help='The file to read in.')
parser.add_argument('--line_number', '-l', type=int, default=1, help='The line number of the line to be printed.')

args = parser.parse_args()
print(args)
print(args.file_name)
print(args.line_number)

try:
    lines = open(args.file_name, 'r').readlines()
    line = lines[args.line_number - 1]
except IndexError:
    print(f"Error: file {args.file_name} doesn't have {args.line_number} lines.")
except IOError as err:
    print(f"Error: {err}")
else:
    print(line)


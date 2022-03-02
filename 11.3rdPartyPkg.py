#!/usr/bin/env python3

import sys
import argparse
from typing import Text
import requests
import json

parser = argparse.ArgumentParser()
parser.add_argument('url', help='URL to store the contents of')
parser.add_argument('filename', help='the filename to store the content under')
parser.add_argument('--content_type', 
                    '-c',
                    default='html',
                    choices=['html','JSON'],
                    help="json or html"
)
args = parser.parse_args()
print(args)

res = requests.get(args.url)
if res.status_code >= 400:
    print(f"Error: {res.status_code}")
    sys.exit(1)

if args.content_type == 'JSON':
    try:
        content = json.dumps(res.json())
    except ValueError:
        print("Error: Content is not JSON")
        sys.exit(1)
else: 
    content = res.text

with open(args.filename, 'w', encoding='UTF-8') as f:
    f.write(content)
    print(f"content is written to {args.filename}")


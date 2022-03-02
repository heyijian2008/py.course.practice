#!/usr/bin/env python3
import random
import os
import json
import glob
import shutil

try:
    os.mkdir('./processed')
except OSError:
    print("'processed' folder already exists.")

try:
    os.mkdir('./new')
except OSError:
    print("'new' folder already exists.")


count = int(os.getenv("FILE_COUNT") or 100)
words = [word.strip() for word in open('/usr/share/dict/words').readlines()]
for identifier in range(count):
    amount = random.uniform(1.0, 1000)
    content = {
        'topic': random.choice(words),
        'value': "%.2f" % amount
    }
    with open(f'./processed/receipt-{identifier}.json', 'w') as f:
        json.dump(content, f)


receipts = glob.glob('./processed/receipt-[0-3]*.json')
subtotal = 0.0

for path in receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    name = path.split("/")[-1]
    dest = f"./new/{name}"
    shutil.move(path, dest)
    print (f"moved {path} to {dest}")

print ("Subtotal: $ %.2f" % subtotal)
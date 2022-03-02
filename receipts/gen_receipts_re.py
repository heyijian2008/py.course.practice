#!/usr/bin/env python3
import random
import os
import json
import glob
import shutil
import math

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


subtotal = 0.0

for path in glob.iglob('./processed/receipt-[4-5]*.json'):
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    dest = path.replace("processed", "new")
    shutil.move(path, dest)
    print (f"moved {path} to {dest}")


print(f"Subtotal: $ {math.ceil(subtotal)}")
print(f"Subtotal: $ {math.floor(subtotal)}")
print(f"Subtotal: $ {round(subtotal, 2)}")
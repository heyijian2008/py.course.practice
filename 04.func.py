#!/usr/bin/env python3
message = input("Please input a message: ")
count   = input("Please input number of repeats [1]: ").strip()

if count: count = int(count)
else: count = 1

def repeat_message(message, count):
    """repeat the message for count times"""
    while count > 0:
        print(f"{message}")
        count -= 1
repeat_message(message, count)
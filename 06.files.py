#!/usr/bin/env python3
def get_file_name (re_prompt=False):
    if re_prompt:
        print("Please input a file name: ")
    file_name = input ("Please input a file name: ").strip()
    return file_name or get_file_name(True)

file_name = get_file_name()

print(f"Please type in your content to be written into {file_name}, end with an empty line.")
lines = []
with open(file_name, 'w') as f_out:
    line = input()
    while line:
        lines.append(f"{line}\n")
        line = input()
    f_out.writelines(lines)
print (f"{len(lines)} of lines are written to file {file_name}")



#!/usr/bin/env python3
users = [
    {"admin" : True,  "active": True,   "name"  : "Jeffrey"},
    {"admin" : False, "active": False,  "name"  : "Jefaaay"},
    {"admin" : True,  "active": False,  "name"  : "Jefbbby"},
    {"admin" : False, "active": True,   "name"  : "Jeccccy"},
]
line_no = 1
for user in users:
    prefix = ''
    if user['admin'] and user['active']:
        prefix = "ACTIVE - (ADMIN) "
    elif user['admin']:
        prefix = "(ADMIN) "
    elif user['active']:
        prefix = "ACTIVE - "
    print(str(line_no) + ': ' + prefix + user['name'])
    line_no += 1



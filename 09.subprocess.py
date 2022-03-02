#!/usr/bin/env python3

import subprocess
import os
import argparse
from sys import exit

# To start a dummy server listening a port: "python3 -m http.server 5500".
# To verify port listening: "lsof -n -i4TCP:5500"

parser = argparse.ArgumentParser(description="kill the running process listen to the given port.")
parser.add_argument('port', type=int, help="the port number to check.")

port = parser.parse_args().port
try:
    result = subprocess.run(
        ['lsof', '-n', '-i4TCP:%s' % port],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
except subprocess.CalledProcessError:
    print(f"No Process is listening to port {port}.")
    exit(1)
else:
    listening = ''
    for line in result.stdout.splitlines():
        if "LISTEN" in str(line): 
            listening = line
            break
    if listening:
        pid = int(listening.split()[1])
        os.kill(pid, 9)
        print (f"Killed process {pid}")
    else:
        print(f"No Process is listening to port {port}.")
        exit(1)


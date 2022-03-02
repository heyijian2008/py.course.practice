#!/usr/bin/env python3
import math
import os

digits = int(os.getenv("DIGITS") or 10)
print(os.getenv("DIGITS"))
print("%.*f"%(digits, math.pi))


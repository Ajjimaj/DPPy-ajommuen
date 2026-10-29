#!/usr/bin/env python3

import sys

# 
if len(sys.argv) > 2:
    # reversed is built-in function
    for arg in reversed(sys.argv[1:]):
        print(arg)
else:
    print("none")

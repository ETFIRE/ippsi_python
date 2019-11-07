#!/usr/bin/python3

"""
def moyenne(a, b):
    return (a/b)


print(moyenne(8, 4))
"""

import os
import sys

print(sys.argv)

#path = "/home/kit"
print(os.path.join("home", "kit"))
dir(os)
for x in dir(os):
	if "dir" in x:
		print(x)


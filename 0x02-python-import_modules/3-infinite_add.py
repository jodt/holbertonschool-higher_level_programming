#!/usr/bin/python3
import sys
arg_list = sys.argv
result = 0
for arg in range(1, len(arg_list)):
    result += int(arg_list[arg])
print(result)

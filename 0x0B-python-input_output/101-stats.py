#!/usr/bin/python3
"""
This is stats module
"""
import sys


count = 0
result = {"200": 0, "301": 0, "400": 0, "401": 0,
          "403": 0, "404": 0, "405": 0, "500": 0}
filesize = 0

try:
    for line in sys.stdin:
        separate_string = line.split()
        if (len(separate_string) >= 2):
            filesize += int(separate_string[-1])
            if separate_string[-2] in result:
                result[separate_string[-2]] += 1
            count += 1
        if count % 10 == 0:
            print("File size: {}".format(filesize))
            for k, v in sorted(result.items()):
                if (v != 0):
                    print("{}: {}".format(k, v))
    print("File size: {}".format(filesize))
    for k, v in sorted(result.items()):
        if (v != 0):
            print("{}: {}".format(k, v))

except KeyboardInterrupt:
    print("File size: {}".format(filesize))
    for k, v in sorted(result.items()):
        if (v != 0):
            print("{}: {}".format(k, v))

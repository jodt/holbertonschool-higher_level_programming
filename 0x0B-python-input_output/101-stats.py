#!/usr/bin/python3
"""
This is stats module
"""
import fileinput

count = 0
result = {"200": 0, "301": 0, "400": 0, "401": 0,
          "403": 0, "404": 0, "405": 0, "500": 0}
filesize = 0

try:
    for line in fileinput.input():
        separate_string = []
        separate_string = line.split(" ")
        filesize += int((separate_string[-1])[:-1])
        for k in result.keys():
            if k in line:
                result[k] += 1
                count += 1
        if count == 10:
            print("File size: {}".format(filesize))
            for k, v in result.items():
                if (v != 0):
                    print("{}: {}".format(k, v))
                    count = 0
except KeyboardInterrupt:
    print("File size: {}".format(filesize))
    for k, v in result.items():
        if (v != 0):
            print("{}: {}".format(k, v))

#!/usr/bin/python3
"""
This is the hbtn_header module
The script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id
"""
import sys
import urllib.request
if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        data = response.getheader('X-Request-Id')
        print(data)

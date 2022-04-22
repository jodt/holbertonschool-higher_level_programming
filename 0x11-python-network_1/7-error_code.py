#!/usr/bin/python3
"""
This is the error_code module
The script takes in a URL, sends a request
to the URL and displays the body of the response.
"""
import sys
import requests
if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url)
    print(r.text if r.ok else "Error code: {}".format(r.status_code))

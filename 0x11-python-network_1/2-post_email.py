#!/usr/bin/python3
"""
This is the post_email module
The script akes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse
if __name__ == '__main__':
    url = sys.argv[1]
    mail = sys.argv[2]
    value = {'email': mail}
    data = urllib.parse.urlencode(value).encode()
    with urllib.request.urlopen(url, data) as response:
        print(response.decode('utf-8'))

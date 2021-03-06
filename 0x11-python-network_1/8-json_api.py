#!/usr/bin/python3
"""
This is the module json_api
The script takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests
if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    value = {'q': sys.argv[1] if len(sys.argv) > 1 else ''}
    r = requests.post(url, data=value)
    try:
        dict = r.json()
        if len(dict):
            print("[{}] {}".format(dict.get('id'), dict.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

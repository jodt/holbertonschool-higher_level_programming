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
    if len(sys.argv) == 1:
        print("No result")
    else:
        url = "http://0.0.0.0:5000/search_user"
        value = {'q': sys.argv[2] if sys.argv[2] else ''}
        try:
            r = requests.post(url, data=value).json()
            if len(r):
                print("[{}] {}".format(r.get('id'), r.get('name')))
            else:
                print("No result")
        except requests.exceptions.JSONDecodeError as e:
            print("Not a valid JSON")

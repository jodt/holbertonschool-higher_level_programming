#!/usr/bin/python3
"""
This is the my_github module
The script takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
import sys
if __name__ == '__main__':
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    token = sys.argv[2]
    r = requests.get(url, auth=(username, token))
    print(r.json().get('id') if r.ok else "None")

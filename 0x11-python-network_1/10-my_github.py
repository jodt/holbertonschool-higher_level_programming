#!/usr/bin/python3
"""
This is the my_github module
The script takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
import sys
if __name__ == '__main__':
    url = 'https://api.github.com/users/octocat'
    token = sys.argv[2]
    username = sys.argv[1]
    r = requests.get(url, data={username: token})
    dict = r.json()
    print(dict.get('id'))

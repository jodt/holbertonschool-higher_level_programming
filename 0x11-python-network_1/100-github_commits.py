#!/usr/bin/python3
"""
This is the module github_commits
"""
import requests
import sys
if __name__ == '__main__':
    user = sys.argv[2]
    repo = sys.argv[1]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(repo, user)
    r = requests.get(url)
    if r.ok:
        list = r.json()
        for i in range(10):
            print("{}: {}".format(list[i].get('sha'), list[i].get(
                'commit').get('author').get("name")))
    else:
        print("None")

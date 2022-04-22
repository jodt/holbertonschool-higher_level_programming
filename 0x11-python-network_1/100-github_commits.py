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
    r = requests.get(url, params={'per_page': 10})
    if r.ok:
        list = r.json()
        for commit in list:
            print("{}: {}".format(commit.get('sha'), commit.get(
                'commit').get('author').get("name")))
    else:
        print("None")

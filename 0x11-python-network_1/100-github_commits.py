#!/usr/bin/python3
"""Lists the 10 recent commis on a github repo
Usage: ./100-github_commits.py <repo name> <repo owner>
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])
    res = requests.get(url)
    commits = res.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass

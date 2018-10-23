#!/usr/bin/env python

import argparse
import requests
from bs4 import BeautifulSoup
from subprocess import call

def get_repositories(username):
    '''
        Returns the public repositories which the given username has registrated on github.com.
        Return format is a list sorted by ascending alphabet
    '''
    url = 'http://github.com/' + username + "?tab=repositories"
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, features="html.parser")
    result = soup.find_all(itemprop="name codeRepository")
    repos = []
    for item in result:
        repos.append(item.get_text().strip())
    repos.sort()
    return repos

def clone_repository(username, reponame):
    '''
        Make system call and clone repository
        - username = githubuser
        - repone = public repository name
    '''
    url = "https://github.com/" + username + "/" + reponame + ".git"
    call(["git", "clone", url, reponame])

parser = argparse.ArgumentParser(description="Lists and lets you clone github repositories")
parser.add_argument("username", help="pass github username to function call")
args = parser.parse_args()

user = str(args.username)
repos = get_repositories(user)
length = len(repos)

print(f"Following public repositories for {user} were found:")
print("---------------------------------")
[print(f"[{repos.index(repo)+1}] {repo}") for repo in repos]
while True:
    choice = input(f"Type 1-{length} for repo to clone or 'q' to quit: ")
    try:
        if choice == "q":
            break 
        elif int(choice) > 0:
            if int(choice) <= int(length):
                repo = repos[(int(choice) - 1)]
                print(f"Cloning into ./{repo}")
                clone_repository(user, repo)
                break
    except TypeError:
        pass
    except ValueError:
        pass
    print("You've entered an invalid value")
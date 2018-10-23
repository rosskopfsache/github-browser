#!/usr/bin/env python

import re
import requests
from bs4 import BeautifulSoup

base = 'http://github.com'
user = "rosskopfsache"

#url = base + "/" + user
url = "https://github.com/rosskopfsache?tab=repositories"
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, features="html.parser")
span = soup.find_all(itemprop="name codeRepository")
repos = []
for item in span:
    repos.append(item.get_text().strip())

'print(repos[0])'
print(repos)


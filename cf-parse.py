import os
import sys
import requests
from bs4 import BeautifulSoup

contest_url1 = 'http://codeforces.com/contest/'
contest_url2 = '{}/my'

contest_id = 1166
contest_url = contest_url1 +  contest_url2.format(contest_id)
print(contest_url)

page = requests.get(contest_url)
# print(page.text)

soup = BeautifulSoup(page.text, 'html.parser')
# print(soup.prettify())

links = soup.findAll('a', attrs={"href" : "/profile/greenindia"})
print(links)




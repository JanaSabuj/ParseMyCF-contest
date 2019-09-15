import os
import sys
import requests
import re
from bs4 import BeautifulSoup

contest_url = 'https://codeforces.com/contests/with/'
username = 'greenindia'
submission_list_url = 'https://codeforces.com/submissions/greenindia/contest/'

contest_url = contest_url + username
print(contest_url)

page = requests.get(contest_url)
soup = BeautifulSoup(page.text, 'html.parser')
# print(soup.prettify())

#extract the datatable 
contests = soup.find('div', attrs={"class":"datatable"})
c_table = contests.find('tbody')
lst = contests.findAll('tr')
total_contests = len(lst) - 1

t = int(input('How many recent contests do you want to parse ?\nEnter : ')) + 1

get_soln_url = "https://codeforces.com/contest/{}/submission/{}"

def get_soln_text(sub_id, contest_id):
    url_soln = get_soln_url.format(contest_id,sub_id)
    print(url_soln)



def extract_solution(row_data, c_id):
    # print(row_data)

    sub_cell = row_data[-3].find('span')
    sub_id = sub_cell['submissionid']
    sub_status = sub_cell.text
    print(sub_id)
    print(sub_status)

    get_soln_text(sub_id,c_id)

    print("\n\n\n")


for i in range(t):
    if i==0: continue
    row = lst[i]
    row_data = row.findAll('td')
    # print(row_data)
    link = row_data[1]
    cname = link.find('a')['title']
    print(cname)

    cnumber = link.find('a')['href']
    val = re.findall('[0-9]+',cnumber)[0]
    print(val)

    sub_lst_url = submission_list_url + val
    print(sub_lst_url)

    new_page = requests.get(sub_lst_url)
    new_soup = BeautifulSoup(new_page.text,'html.parser')
    # print(new_soup.prettify())

    new_contests = new_soup.find('div', attrs={"class":"datatable"})
    new_sub_table = new_contests.find('tbody')
    new_lst = new_contests.findAll('tr')
    total_subs = len(new_lst) - 1
    print("\n\n\n\n\n")
    for i in range(len(new_lst)):
        if i == 0:continue
        new_row = new_lst[i]
        new_row_data = new_row.findAll('td')
        # print(new_row_data)
        extract_solution(new_row_data, val)






    

    
    
    
    
    
    
 
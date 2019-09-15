import os
import sys
import requests
import re
from bs4 import BeautifulSoup
import shutil

parent_path = os.getcwd()

contest_url = 'https://codeforces.com/contests/with/'
username = input('Enter your Codeforces username: ')
submission_list_url = 'https://codeforces.com/submissions/{}/contest/'.format(username)

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

def make_dir_os(sub_id, contest_id, sub_status,sub_name,sub_lang, contest_name, get_soln):
    folder_name = os.path.join(parent_path , contest_name)
    print(folder_name)

    ext = ""
    if 'C++' in sub_lang:
        ext = ".cpp"
    sub_name = sub_name + ext
    file_name = os.path.join(folder_name,sub_name)
    print(file_name)
    
    file1 = open(file_name,'a')
    header = "\n\n\n" + contest_id + " " + sub_name + " " + sub_lang + " " + sub_status + "\n\n\n"
    file1.write( header + get_soln)
    file1.close()



    


def get_soln_text(sub_id, contest_id, sub_status,sub_name,sub_lang, contest_name):
    url_soln = get_soln_url.format(contest_id,sub_id)
    print(url_soln)

    cpp = requests.get(url_soln)
    soup_cpp = BeautifulSoup(cpp.text,'html.parser')
    # print(soup_cpp.prettify())
    get_soln = soup_cpp.findAll('div',attrs={"class" : "roundbox"})[1].find('pre').text
    # print(get_soln)

    make_dir_os(sub_id, contest_id, sub_status,sub_name,sub_lang, contest_name,get_soln)

    # print("\n\n\n-------\n\n\n")



def extract_solution(row_data, c_id, contest_name):
    # print(row_data)

    sub_cell = row_data[-3].find('span')
    sub_id = sub_cell['submissionid']
    sub_status = sub_cell.text
    sub_name = row_data[-5].find('a').text.strip()
    sub_lang =  row_data[-4].text.strip()
    # print(sub_name)
    print(sub_id)
    print(sub_status)
    print(sub_name)
    print(sub_lang)

    get_soln_text(sub_id,c_id,sub_status,sub_name,sub_lang, contest_name)

    print("\n\n\n")

# loop through each of the contests 
for i in range(t):
    if i==0: continue
    row = lst[i]
    row_data = row.findAll('td')
    # print(row_data)
    link = row_data[1]
    cname = link.find('a')['title']
    # print(cname)

    cnumber = link.find('a')['href']
    val = re.findall('[0-9]+',cnumber)[0]
    # print(val)

    sub_lst_url = submission_list_url + val
    # print(sub_lst_url)

    new_page = requests.get(sub_lst_url)
    new_soup = BeautifulSoup(new_page.text,'html.parser')
    # print(new_soup.prettify())

    new_contests = new_soup.find('div', attrs={"class":"datatable"})
    new_sub_table = new_contests.find('tbody')
    new_lst = new_contests.findAll('tr')
    total_subs = len(new_lst) - 1
    # print("\n\n\n\n\n")

    folder_name = os.path.join(parent_path,cname)
    os.chdir(parent_path)

    if os.path.exists(folder_name) == False:
        os.mkdir(folder_name)

    for i in range(len(new_lst)):
        if i == 0:continue
        new_row = new_lst[i]
        new_row_data = new_row.findAll('td')
        # print(new_row_data)
        extract_solution(new_row_data, val, cname)








    

    
    
    
    
    
    
 
# Built by greenindia - Sabuj Jana - Jadavpur University 
# www.janasabuj.github.io
import os
import sys
import requests
import re
from bs4 import BeautifulSoup
import shutil
import time

parent_path = os.getcwd()
illegal = ["<", ">", "[", "]",  "?", ":", "*" , "|"]

contest_url = 'http://codeforces.com/contests/with/'
username = input('Enter your Codeforces username: ')
submission_list_url = 'http://codeforces.com/submissions/{}/contest/'.format(username)
contest_url = contest_url + username

#visit the list of past contests page
page = requests.get(contest_url)
if (page.status_code != 200):
    print("Failed to retrieve the URL: {}".format(contest_url))
    exit(1)
soup = BeautifulSoup(page.text, 'html.parser')

#extract the datatable 
contests = soup.find('div', attrs={"class":"datatable"})
c_table = contests.find('tbody')
lst = contests.findAll('tr')
total_contests = len(lst) - 1
print("{} has participated in {} contests".format(username,total_contests))

# function to get the code extension 
def getExt(sub_lang):
    ext = ""
    if 'C++' in sub_lang:
        ext = ".cpp"
    elif 'C' in sub_lang:
        ext = ".c"
    elif 'Py' in sub_lang:
        ext = ".py"
    elif "JavaScript" in sub_lang:
        ext = ".js"
    elif "Java" in sub_lang:
        ext = ".java"
    elif "Kotlin" in sub_lang:
        ext = ".kt"
    elif "PHP" in sub_lang:
        ext = ".php"
    elif "Rub" in sub_lang:
        ext = ".rb"
    
    return ext

#function to create misc info file in contest folder    
def createInfoFile(folder_name,username, info_arr):
    info_file =os.path.join(folder_name,"contest-info-on-{}.txt".format(username))
    fname = open(info_file, "a")
    txt_to_write = ""
    for txt in info_arr:
        txt_to_write = txt_to_write + txt + "\n"
    fname.write(txt_to_write)
    fname.close()

#creating the contest-folder
def createFolder(folder_name):
    if os.path.exists(folder_name) == False:
        os.mkdir(folder_name)
        print("Folder created for contest {}".format(i))
        return 1
    else:
        print("Pass !!! Already exits !!!")
        return 0

#info-arr-extraction
def info_arr_extraction(row_data):
    info_arr = []
    m_0 = "Contest no: " + row_data[0].text.strip()
    m_1 = "Contest name: " + row_data[1].find('a')['title'].strip()
    m_2 = "Rank: " + row_data[2].find('a').text.strip()
    m_3 = "Solved: " + row_data[3].find('a').text.strip()
    m_4 = "Rating Change: " + row_data[4].find('span').text.strip()
    m_5 = "New Rating: " + row_data[5].text.strip()
    m_user = "Username: " + username

    info_arr.append(m_user)
    info_arr.append(m_0)
    info_arr.append(m_1)
    info_arr.append(m_2)
    info_arr.append(m_3)
    info_arr.append(m_4)
    info_arr.append(m_5)

    return info_arr

#function to create a directory tree with folder + files
def make_dir_os(sub_id, contest_id, sub_status,sub_name,sub_lang, contest_name, get_soln,folder_name):
    # folder_name = os.path.join(parent_path , contest_name)

    #func 
    ext = getExt(sub_lang)

    sub_name = sub_name + ext
    file_name = os.path.join(folder_name,sub_name)
    
    file1 = open(file_name,'a')
    header = "\n" + contest_id + " " + sub_name + " " + sub_lang + " " + sub_status + "\n"
    file1.write(header + get_soln)
    file1.close()

#function to extract the submitted code
def get_soln_text(sub_id, contest_id, sub_status,sub_name,sub_lang, contest_name,folder_name):
    url_soln = get_soln_url.format(contest_id,sub_id)
    print(url_soln)

    cpp = requests.get(url_soln)
    soup_cpp = BeautifulSoup(cpp.text,'html.parser')
    
    get_soln = soup_cpp.findAll('div',attrs={"class" : "roundbox"})[1].find('pre').text
    make_dir_os(sub_id, contest_id, sub_status,sub_name,sub_lang, contest_name,get_soln,folder_name)

#driver function to call the get_soln_text function
def extract_solution(row_data, c_id, contest_name,folder_name):
    # print(row_data)
    sub_cell = row_data[-3].find('span')
    sub_id = sub_cell['submissionid']
    sub_status = sub_cell.text
    sub_name = row_data[-5].find('a').text.strip()
    sub_lang =  row_data[-4].text.strip()
    
    #log
    print(sub_id)
    print(sub_status)
    print(sub_name)
    print(sub_lang)

    get_soln_text(sub_id,c_id,sub_status,sub_name,sub_lang, contest_name,folder_name)

    print("\n")

#MAIN
#Ask how many recent contests to parse?? 
#If folder already parsed before, it'll be skipped!
t = int(input('How many recent contests do you want to parse ?\nEnter : ')) + 1
get_soln_url = "http://codeforces.com/contest/{}/submission/{}"

# loop through each of the contests 
for i in range(t):
    if i==0: continue #This is the row header row - ignore
    row = lst[i]
    row_data = row.findAll('td')

    #get all info about the contest - f1
    info_arr = info_arr_extraction(row_data)

    link = row_data[1]
    cname = link.find('a')['title']
    cnumber = link.find('a')['href']
    val = re.findall('[0-9]+',cnumber)[0] #regex

    sub_lst_url = submission_list_url + val

    #New submission page visited
    new_page = requests.get(sub_lst_url)
    if new_page.status_code !=200:
        print("This {} cannot be parsed !! ".format(cname))
        continue
    new_soup = BeautifulSoup(new_page.text,'html.parser')

    new_contests = new_soup.find('div', attrs={"class":"datatable"})
    new_sub_table = new_contests.find('tbody')
    new_lst = new_contests.findAll('tr')
    total_subs = len(new_lst) - 1

    #Maketh the parent folder
    cname = cname + " by User: {}".format(username)
    folder_name = os.path.join(parent_path,cname)
    os.chdir(parent_path)

    for str_char in illegal:
        folder_name = folder_name[:10] + folder_name[10:].replace(str_char, " ")

    if createFolder(folder_name) == 0:
        continue

    # take some rest my script
    print("\nTime to rest for 5 secs !!!\n")
    time.sleep(5)
    # time to roll    
    
    createInfoFile(folder_name,username,info_arr)   

    for i in range(len(new_lst)):
        if i == 0:continue
        new_row = new_lst[i]
        new_row_data = new_row.findAll('td')
        extract_solution(new_row_data, val, cname,folder_name)

    #Wish you high rating on the next contest!!!!
import os
import sys
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

username = 'greenindia'
pw = 'sabujjana1998'
# getting selenium webdriver from chrome
chromedriver = "/home/sabuj/Downloads/SD/chromedriver"
browser = webdriver.Chrome(chromedriver)
browser.get('http://www.codeforces.com/')

#login
enter = browser.find_element_by_css_selector('#header > div.lang-chooser > div:nth-child(2) > a:nth-child(1)')
enter.click() 
browser.implicitly_wait(20)
print("Entered main site !!!")

handle = browser.find_element_by_css_selector('#handleOrEmail')
handle.send_keys(username)
print('handle entered')
browser.implicitly_wait(10)

passwd = browser.find_element_by_id('password')
passwd.click()
passwd.send_keys(pw)
print('Password Entered !!! ')

browser.find_element_by_class_name("submit").click()
print('Submitted !!')
#end-of-login

#contest-scrape
browser.implicitly_wait(10)
user = browser.find_element_by_css_selector('#header > div.lang-chooser > div:nth-child(2) > a:nth-child(1)')
user.click()
print('User page entered!!!')

#contests
browser.implicitly_wait(20)
# contests = browser.find_element_by_css_selector('#pageContent > div.second-level-menu > ul > li:nth-child(10) > a')
# contests.click()
# print('Users Contest Page list opened')

# #page-manipulation
# browser.implicitly_wait(15)
# fname = browser.find_elements_by_tag_name('table')
# fname = fname.get_attribute('class')
# print(fname)










# codeforces-parser-by-sabuj-jana
A personal submission parser for CF, parsed by individual contests.

> **Inspiration** 
> Why work hard when Python is your pet ? 

# What it does
* You are prompted the username
    * You are shown the no of contests the user has participated
    * You **enter** the no of recent contests you want to parse 
* The script starts scraping from the most recent contests
* For every contest, A Folder is created having the format (name + username)
    * Each folder has all the submissions with their proper extensions.
    * Each problem has all its attempts(WA,AC,TLE,RE,ME) in serial order separated by appropriate         delimiters
    * A contest-info .txt file is also created having all the miscellaneous information about the
      user's performance like - Rating Change, New rating, Rank, Problems successfully solved etc.
* If a folder was previously present i.e a contest was previously parsed by this scraper, it'll ignore    the contest and move one to the next unfinished contest

# What to do
* Download the cf.py file 
* Install latest version of python (add to PATH) if not already installed
* Pip install all the below mentioned modules and dependencies
* Place the script in a folder where you want all the different folders of contest
* **Bonus** - If you place it in a **git initialised repository**, after the script finishes, you can simply commit all the changes and all your contest-codes will be pushed to github
* An active internet connection while the script parses

## Requirements
* Modules
    * os
    * sys
    * requests
    * re
    * bs4 (BeautifulSoup)
    * time

* User Requiremets
    * codeforces-user-id of any person

* Python Version
    * 3 or above

* Active internet when py - script runs

* The terminal (required for input) shows log as the script runs


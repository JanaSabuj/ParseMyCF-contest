# ParseMyCf-contest
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

# Script prompting the username
![1](https://user-images.githubusercontent.com/39147514/65044905-7219a980-d97b-11e9-9256-21bc4c4d1d58.png)

# Script prompting for no of contests
![cf2](https://user-images.githubusercontent.com/39147514/65045330-36331400-d97c-11e9-9d06-dbca202d2ce2.png)

# What to do
* Download only the **cf.py** file 
* Install latest version of python (add to PATH) if not already installed
* **Pip install** all the **below mentioned modules** and dependencies
* Place the script in a folder where you want all the different folders of contest
* Run **python3 cf.py** or **python cf.py** as suitable
* **Bonus** - If you place it in a **git initialised repository**, after the script finishes, you can simply commit all the changes and all your contest-codes will be pushed to github
* An active internet connection while the script parses

# Middle of file parsing (has scraped 1 contest till now..)
![45](https://user-images.githubusercontent.com/39147514/65045096-ce7cc900-d97b-11e9-90e5-17a9ede25ff6.png)

# Middle of parsing(has scraped 2 contests till now..)
![4545](https://user-images.githubusercontent.com/39147514/65045430-64185880-d97c-11e9-90ce-a6c2553192ba.png)

# End of parsing 
![4564](https://user-images.githubusercontent.com/39147514/65045480-7a261900-d97c-11e9-8ca9-8c71f01eae44.png)

# Peek inside the directory structure of a contest
![101](https://user-images.githubusercontent.com/39147514/65045540-9c1f9b80-d97c-11e9-9fdd-854269d1dc50.png)
![456456](https://user-images.githubusercontent.com/39147514/65045565-a9d52100-d97c-11e9-83e5-94b7453f3c1c.png)

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


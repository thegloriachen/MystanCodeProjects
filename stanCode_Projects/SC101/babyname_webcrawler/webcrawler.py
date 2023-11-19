"""
File: webcrawler.py
Name: Gloria
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        # tags = soup.find_all("table", {"class": "t-stripe"})
        boys = 0
        girls = 0
        tags = soup.find_all('tr')
        for tag in tags:
            tag = tag.text.split()
            if len(tag) == 5 and tag[0] != "Rank":
                boys += int(string_manipulation(tag[2]))
                girls += int(string_manipulation(tag[4]))
        print("Male Number: " + str(boys))
        print("Female Number: " + str(girls))


def string_manipulation(tag):
    """
    Given a number of baby name data (string type), and remove the comma symbol from the string.

    Input:
        tag (str): The number of baby name data.

    Returns:
        ans (str): The str which was removed the comma symbol.
    """
    ans = ""
    for ch in tag:
        if ch.isdigit():
            ans += ch
    return ans


if __name__ == '__main__':
    main()

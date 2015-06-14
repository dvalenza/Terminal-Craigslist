import re 
import urllib2
from bs4 import BeautifulSoup
import os,sys

         
counter = 0
page = urllib2.urlopen("http://www.craigslist.org/about/sites").read()
soup = BeautifulSoup(page)
f = open(sites.py),"a")
counter+=1
for x in range (0,10):
    try:
        mainSoup = soup.findAll('div', attrs={ 'class':'colmask'})
        soup2 = BeautifulSoup(str(mainSoup))
        location = str(soup2.findAll('h4')[x].contents.pop())
        for y in range(0,10):
            try:
                sublocation = str(soup2.findAll('ul')[y].contents.pop())
            except IndexError:
                break
        data  = 
    except IndexError:
      break

    f.write(data)
f.close()


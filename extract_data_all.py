############################################################
#Extracs each Craigslist category eg. Boston, NY  .. for sale, wanted.. 
#and puts in single file "alldata". also formats it in list format.
#
#Must be combined with data from extract_data_into_list.py
#(alldata2.py) to create a full cllist.py
#
#EX Output:
#"boston",
#"albany, NY",
#"cape cod",
#"catskills",
#"central NJ",
#"eastern CT",

import re 
import urllib2
from bs4 import BeautifulSoup
import os,sys
import cllib 

page = urllib2.urlopen('http://boston.craigslist.org/search/ccc').read()
soup = BeautifulSoup(page)
f = open('alldata',"a")
for x in range (0,100):
    try:
      data = "\""+str((soup.findAll("option")[x].contents.pop()))+"\",\n"
    except IndexError:
      break

    f.write(data)
f.close()
  

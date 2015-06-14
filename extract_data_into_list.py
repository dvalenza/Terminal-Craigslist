###########################################################
#Makes a file cllist_list.py containing scraped CL data
#
#Does not include and location, and must be combined with 
#Data from Extract_data_all.py (alldata file )to make a full cllist.py 
#
#EX Output:
#community=["all",
#"activity partners",
#"artists",
#"childcare",
#.....
#]
#
#events=["all",
#"classes",
#"events",
#]
#
#for_sale=["all",
#"antiques",
#"appliances",
#"arts+crafts",
#"atvs/utvs/snow",
#....

import re 
import urllib2
from bs4 import BeautifulSoup
import os,sys
import cllib

counter = 0
f = open("alldata2.py","a")
for i in cllib.section:
  f.write(str(cllib.section[counter][0])+"=[")
  page = urllib2.urlopen(cllib.section[counter][1]).read()
  soup = BeautifulSoup(page)
  counter+=1
  for x in range (42,100):
    try:
      data = "\""+str((soup.findAll("option")[x].contents.pop()))+"\",\n"
    except IndexError:
      break
    f.write(data)
  f.write("]\n\n")
f.close()
  

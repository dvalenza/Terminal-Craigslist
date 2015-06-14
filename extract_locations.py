###############################################################


import re 
import urllib2
from bs4 import BeautifulSoup
import os,sys
import cllib

         
counter = 0
page = urllib2.urlopen(cllib.section[0][1]).read()
soup = BeautifulSoup(page)
f = open("sublocationURLS","a")
counter+=1
for x in range (0,50):
    try:
      data = "(\""+str((soup.findAll("option")[x].contents.pop()))+"\",\""+str(soup.findAll("option")[x].attrs.values().pop())+'\"),\n'
    except IndexError:
      break
    
    f.write(data)
f.close()
  

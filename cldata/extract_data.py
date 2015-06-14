import re 
import urllib2
from bs4 import BeautifulSoup
import os,sys
import cllib 

         
#location = soup.findAll('select', attrs={ 'name':'areaAbb'})
counter = 0
for i in cl
lib.section:
  page = urllib2.urlopen(cllib.section[counter][1]).read()
  soup = BeautifulSoup(page)
  f = open(str(cllib.section[counter][0]),"a")
  counter+=1
  for x in range (42,100):
    try:
      data = "(\""+str((soup.findAll("option")[x].contents.pop()))+"\",\""+str(soup.findAll("option")[x].attrs.values().pop())+'\"),\n'
    except IndexError:
      break

    f.write(data)
  f.close()
  

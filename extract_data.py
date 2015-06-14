###############################################################
#Makes a list of touples pairs of each sub listing 
#in seperate files (later combined to form cllib)
#
#Individual File Names: community, gigs, for sale...
#
#Ex Output: 
#("all","ccc"),
#("activity partners","act"),
#("artists","ats"),
#("childcare","kid"),
#("general","com"),
#

import re 
import urllib2
from bs4 import BeautifulSoup
import os,sys
import cllib 

         
counter = 0
for i in cllib.section:
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
  

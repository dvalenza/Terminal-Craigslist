#Example of using curses library wrapper.
#watches for keypress tab and displays string hi and q=quit

import re 
import urllib2
from bs4 import BeautifulSoup
import os,sys
import cllib 
import curses


def main(c):
    pos = 0
    while 1:
      x = c.getch()
      if (x == ord('\t')):
         if pos == 0:
             string = ""
             for wrd in cllib.section:
                 string += (wrd[0] + " ")
             c.addstr(string)
      elif (x == ord('q')):
        break
    curses.endwin()

c = curses.initscr()
if __name__=='__main__':
    curses.wrapper(main)

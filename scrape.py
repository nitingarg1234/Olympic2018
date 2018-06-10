import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# -*- coding: utf-8 -*-
# coding: utf8 
# coding=utf-8
from urllib2 import Request, urlopen
import pandas as pd
from bs4 import BeautifulSoup as soup
filename = "Medal_table.csv"
f= open(filename, "a") 
headers = "RANK,NOC,GOLD,SILVER,BRONZE,TOTAL\n"
f.write(headers)
url = 'https://en.wikipedia.org/wiki/2018_Winter_Olympics_medal_table'
print(url)
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
urlopen(req).close()
page_soup = soup (webpage,"html.parser")
containers = page_soup.findAll('tr')
length= len(containers)
print(length)  
print(containers[5])
for n in range(5,35):
   row= containers[n]
   td_row= row.findAll("td")
   th_row= row.findAll("th")
   print('-----------')	
   RANK = td_row[0].text
   print("RANK: " + RANK)
   NOC = th_row[0].text
   print("NOC: " + NOC)	
   GOLD = td_row[1].text
   print("GOLD: " + GOLD)
   SILVER = td_row[2].text
   print("SILVER: " + SILVER)
   BRONZE = td_row[3].text
   print("BRONZE: " + BRONZE)
   try:
	TOTAL = td_row[4].text
	print("TOTAL: " + TOTAL)
   except:
	RANK= FINAL_RANK
	NOC= th_row[0].text
	GOLD= td_row[0].text
	SILVER=td_row[1].text
	BRONZE= td_row[2].text
	TOTAL= td_row[3].text

   FINAL_RANK= RANK
   FINAL_NOC = NOC
   FINAL_GOLD = GOLD
   FINAL_SILVER=SILVER
   FINAL_BRONZE = BRONZE
   FINAL_TOTAL = TOTAL	
   f.write (FINAL_RANK + ","+ FINAL_NOC.replace(" ","")+","+FINAL_GOLD+","+FINAL_SILVER+","+FINAL_BRONZE+","+FINAL_TOTAL+ "\n")
f.close()
df = pd.read_csv("Medal_table.csv")
print(df)

"""	

"""


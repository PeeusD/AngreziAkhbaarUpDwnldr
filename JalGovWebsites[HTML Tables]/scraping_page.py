
from bs4 import BeautifulSoup 
import requests
from random import randint
url = "https://ejalshakti.gov.in/IMISReports/Reports/basicinformation/rpt_RWS_VillagewisePWSReport.aspx?Rep=0"
headers = [{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'},
        { 'User-Agent' :'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'},
                             { 'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'},
                             { 'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'},
                             { 'User-Agent' :'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'},
                             { 'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}]

res = requests.get(url, headers=headers[randint(0,3)])

soup = BeautifulSoup(res.text, 'html.parser')

allStates_table = soup.select('.ReportTable td')  #list splitted on the basis of each 'td'

lst=[]
j=10


import csv
# name of csv file 
filename = "jal_records.csv"
    
for i in range(len(allStates_table)):
    lst.append(allStates_table[i].text.strip())
    if i==j:
        # writing to csv file 
        with open(filename, 'a', newline='') as csvfile: 
            # creating a csv writer object 
            csvwriter = csv.writer(csvfile)  
            # writing the data rows 
            csvwriter.writerow(lst)
            j +=11
            lst=[]   
 
print("Done!")





 

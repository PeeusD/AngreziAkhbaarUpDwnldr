from bs4 import BeautifulSoup
import requests
import time, random, datetime
import schedule

print("----> RUNNING UR PYTHON SCRAPPER SCHEDULLER...")

dwld_status = False    
        
url =  [
               # scrapping these webapages on by one...
       
        ["https://dailyepaper.in/hindu-analysis-notes-in-pdf-2022/", dwld_status],
        ["https://dailyepaper.in/times-of-india-epaper-pdf-download-2022/", dwld_status],
        ["https://dailyepaper.in/economic-times-newspaper-today", dwld_status],
        ["https://dailyepaper.in/financial-express-newspaper", dwld_status],
        ["https://dailyepaper.in/deccan-chronicle-epaper", dwld_status],  
        ["https://dailyepaper.in/the-tribune-epaper", dwld_status],
        ["https://dailyepaper.in/statesman-newspaper-today", dwld_status],
        ["https://dailyepaper.in/the-asian-age-epaper", dwld_status],
        ["https://dailyepaper.in/telegraph-newspaper",dwld_status] 
        ]

def reset_url_status():
    for i in range(len(url)):
        url[i][1] = dwld_status
    print("-->RAN RESET FUNC....<----")

def schedulling_fun():   

    try:
        for i in range(len(url)):        
                            # applying random headers to avoiding flood errors..
                headers = [{ 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36' },
                             { 'User-Agent' :'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'},
                             { 'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'},
                             { 'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'},
                             { 'User-Agent' :'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'},
                             { 'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'} ]   
                

                rand_heads = random.randint(0,4)  # --->  randint() includes both params values....
            
                print(url[i][0])

                #random delay request to act as human...
                time.sleep(random.randint(10,20))
                        
                today_dt = datetime.datetime.now()
                today_dt = today_dt.strftime("%d")
                if today_dt[0]=="0":
                    today_dt = today_dt.replace("0","")        
                if url[i][1] == dwld_status: #chhecking that ppr already uploaded or not.... 
                        res = requests.get(url[i][0], headers = headers[rand_heads])  
                        if res.status_code == 200 :
                            print(res)
                            soup = BeautifulSoup(res.text,'html.parser')
                                
                          
                            all_links = soup.select(".entry-content p span a")
                            d_link =[]
                            for i in range(7):
                                d_link.append(all_links[i].get('href'))
                                print(f'link {d_link[i]}')
                         
  
                        else:
                            print("website down")         
                else :
                    print("Epaper already uploaded!")
    except Exception as err:
            print('Error: ', err)



# schedule.every(15).minutes.do(schedulling_fun)
# schedule.every().day.at("12:15").do(reset_url_status)    #  reset_url_status
#schedule.every().day.at("01:40").do(schedulling_fun)   # FOR HEROKU/ PYTHON ANYWHERE DEPLOYMENT SET TO IST 07:10
schedulling_fun()    #for debugging USE THIS FUNCTION   

while True:
  
    schedule.run_pending()
    time.sleep(1)            










        

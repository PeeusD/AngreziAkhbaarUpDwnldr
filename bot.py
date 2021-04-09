from bs4 import BeautifulSoup
import requests
import time, random, datetime
from telegram import Bot, ParseMode
from telegram.ext import Updater
from os import getenv
from dotenv import load_dotenv
load_dotenv()
import schedule

TOKEN = getenv('TOKEN')
chat_id = getenv('CHAT_ID')
bot = Bot(token=TOKEN)

print("----> RUNNING UR PYTHON SCRAPPER SCHEDULLER...")
    
        
url =  [
               # scrapping these webapages on by one...
        ["https://dailyepaper.in/the-hindu-pdf-epaper-download", False],
        ["https://dailyepaper.in/indian-express-epaper", False],
        ["https://dailyepaper.in/times-of-india-epaper-pdf-download-2020", False],
        ["https://dailyepaper.in/economic-times-newspaper-today", False],
        ["https://dailyepaper.in/financial-express-newspaper", False],
        ["https://dailyepaper.in/deccan-chronicle-epaper", False],  
        ["https://dailyepaper.in/the-tribune-epaper", False],
        ["https://dailyepaper.in/statesman-newspaper-today", False],
        ["https://dailyepaper.in/the-asian-age-epaper", False],
        ["https://dailyepaper.in/telegraph-newspaper",False] ]

def reset_url_status():
    for i in range(len(url)):
        url[i][1] = False
    print("ran ur reset func")

        

def schedulling_fun():               

        for i in range(len(url)):        

                            # applying random headers to avoiding flood errors..
                headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36' }
                              
                

                # rand_heads = random.randint(0,4)  # --->  randint() includes both params values....
            
                print(url[i][0])
                res = requests.get(url[i][0], headers = headers)

            
                if res.status_code == 200 :
                    print(res)
                    soup = BeautifulSoup(res.text,'html.parser')


                        #checking condition for the hindu....
                    if i == 0:
                        all_links = soup.select(".entry-content.mh-clearfix p a")

                        nxtpglink = all_links[4].get('href')
                        print(nxtpglink)
                    else:      #else other epaper will come here

                        all_links = soup.select(".entry-content p span a")
                        #random delay between both the fetching request 
                    
                        nxtpglink = all_links[0].get('href')
                        print(nxtpglink)
                    
              
                    time.sleep(random.randint(5,9))

                    #moving to next page....
                    
                    if nxtpglink.find("?") > 5:  #checking for updated link...
                            res = requests.get(nxtpglink, headers = headers)
                            
                            soup = BeautifulSoup(res.text,'html.parser')
                            links = soup.find_all("iframe")
                        
                            for link in links:
                                
                                
                                full_dwnldlink = link['src']
                                dwnldlink = link['src'].split("?")
                            
                                ppr_name = dwnldlink[0].split("/")
                                

                                ttl_siz = len(ppr_name)-1
                                ppr_name = ppr_name[ttl_siz]
                                print("Captured Downldlink ---> ",full_dwnldlink)
                                print(ppr_name)
                            


                            today_dt = datetime.datetime.now()

                            today_dt = today_dt.strftime("%d").replace("0","")
                        
                            #checking with todays date with the uploaded date
                            if int((ppr_name.replace("2021","").find(today_dt))) > 1 :
                                    #downloading...
                                
                                # res = requests.get(full_dwnldlink, stream = True)
                                # open('myfile/paper.pdf', 'wb').write(res.content)
                        

                                msg = '<b>'+ ppr_name +"\n\nJOIN NOW:\t @allepaperadda\nOr Search:\t\tallepaperadda\n\n" +'</b>'+ full_dwnldlink
                                print('Downloaded...OK')
                                
                                time.sleep(2)
                                    #uploading to telegram channel...
                                
                                # bot.send_document(chat_id = chat_id, document = open('myfile/paper.pdf', 'rb'), caption = ppr_name +'@mychannel_link')
                                if url[i][1] == False:
                                    bot.send_message(chat_id = chat_id, text = msg, parse_mode = ParseMode.HTML )
                                    print(' Uploaded!...OK')
                                    url[i][1] = True
                                else :
                                    print("Epaper already uploaded!")


                            else :
                                print("Not uploaded yet....last Epaper was: ", ppr_name)

                            #delay between next page which to be scrappped
                    else:
                        print("Something error happend in links...")
                    
                    time.sleep(random.randint(10,20))



       
                else:
                        print("website down")         

schedule.every().day.at("01:30").do(reset_url_status)   #IST 07:00
schedule.every().day.at("01:40").do(schedulling_fun)   # FOR HEROKU/ PYTHON ANYWHERE DEPLOYMENT SET TO IST 07:10
schedule.every().day.at("02:00").do(schedulling_fun)   #IST 07:30
schedule.every().day.at("02:15").do(schedulling_fun)    #IST 07:45
schedule.every().day.at("02:35").do(schedulling_fun)     #IST 08:05 #####  <--------------  CHANGE HERE FOR DEBUGGING  ------>
schedule.every().day.at("02:50").do(schedulling_fun)    #IST 08:20

while True:
  
    # Checks whether a scheduled task... 
    #... is pending to run or not
    schedule.run_pending()
    time.sleep(1)            


updater = Updater(TOKEN)  
updater.start_polling()
updater.idle()






        

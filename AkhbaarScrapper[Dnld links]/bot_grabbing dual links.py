from bs4 import BeautifulSoup
import requests
import time, random, datetime
import schedule

print("----> RUNNING UR PYTHON SCRAPPER SCHEDULLER...")
    
        
url =  [
               # scrapping these webapages on by one...
        ["https://dailyepaper.in/the-hindu-pdf-free-download-25-nov-2021", False],
        ["https://dailyepaper.in/hindu-analysis-notes-in-pdf-download-oct-2021", False],
        ["https://dailyepaper.in/times-of-india-epaper-pdf-download-2020", False],
        ["https://dailyepaper.in/economic-times-newspaper-today", False],
        ["https://dailyepaper.in/financial-express-newspaper", False],
        ["https://dailyepaper.in/deccan-chronicle-epaper", False],  
        ["https://dailyepaper.in/the-tribune-epaper", False],
        ["https://dailyepaper.in/statesman-newspaper-today", False],
        ["https://dailyepaper.in/the-asian-age-epaper", False],
        ["https://dailyepaper.in/telegraph-newspaper",False] 
        ]

def reset_url_status():
    for i in range(len(url)):
        url[i][1] = False
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
                if url[i][1] == False: #chhecking that ppr already uploaded or not.... 

                        res = requests.get(url[i][0], headers = headers[rand_heads])  
                        if res.status_code == 200 :
                            print(res)
                            soup = BeautifulSoup(res.text,'html.parser')
                                #checking condition for the hindu....
                            #if i == 0:
                                #all_links = soup.select(".entry-content.mh-clearfix p a")
                               # newlinks = soup.select("h4~ p")
                               # newlinks = str(newlinks[0]).find("<a href")
                               # nxtpglink = all_links[4].get('href')
                                #print(newlinks)

                              #  if nxtpglink.find("drive") > 5 and newlinks > 0:     #drive link checking...
                                 #   bot.send_message(chat_id = chat_id, text = "<b>The HINDU G-drive link:\tJoin:\t@allepaperadda</b>\n"+ nxtpglink, parse_mode = ParseMode.HTML )
                                 #   print(' Uploaded!...OK')
                                  #  url[i][1] = True

                             #   else:
                                #    print("This is vk.com link")    
                                         #skip the vk.com link as drivelink present....
                          #  else:      #else other epaper will come here

                            all_links = soup.select(".entry-content p span a")

                                #random delay between both the fetching request 
                            d_link = all_links[0].get('href')
                            print("first pg link >",d_link)
                            time.sleep(random.randint(5,12))

                            
                            #moving to next page....
                            if d_link.find("vk.com") > 5: # verifying next pg vk.com link...
                                if d_link.find("?") > 5:  #checking for updated link...
                                        res = requests.get(d_link, headers = headers[rand_heads])
                                            
                                        soup = BeautifulSoup(res.text,'html.parser')
                                        links = soup.find_all("iframe")
                                        
                                        for link in links:    
                                            full_dwnldlink = link['src']
                                            dwnldlink = link['src'].split("?")
                                            
                                            ppr_name = dwnldlink[0].split("/")
                                            ttl_siz = len(ppr_name)-1
                                            ppr_name = ppr_name[ttl_siz]
                                                # print("Captured Downldlink ---> ",full_dwnldlink)
                                            # print(ppr_name)
                                            #checking with todays date with the uploaded date
                                        if int((ppr_name.replace("2021","").find(today_dt))) > -1 :
                                            
                                                msg = f" Paper Name-> {ppr_name} Link-> {full_dwnldlink}"
                                                print('Status..OK\n', msg)
                                                url[i][1] = True
                        
                                                time.sleep(random.randint(2,4)) #delay between next page which to be scrappped
                                        else :
                                            print("Not uploaded yet....last Epaper was: ", ppr_name)

                            #elif nxtpglink.find("drive") > 5 :
                                    #print("Hindu gdrive link posted! its not vk.com link")
                            else:
                                print("Something error happend in links...") 
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










        

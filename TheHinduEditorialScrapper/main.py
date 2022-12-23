from urllib import request
# from dictionary import word_searching
from bs4 import BeautifulSoup as bs
import requests, random
import time
import json
# scrapping articles
url = 'https://www.thehindu.com/opinion/editorial/feeder/default.rss'
headers = [{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'},
            { 'User-Agent' :'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'},
                                { 'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'},
                                { 'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'},
                                { 'User-Agent' :'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'},
                                { 'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}]

res = requests.get(url, headers=headers[random.randint(0,5)])
soup = bs(res.content, features='xml')
all_contents = soup.find_all('item')
# print(all_contents)
items=[]
for i, content in enumerate(all_contents):
    i+=1
    time.sleep(3)
    nxtPageRes = requests.get(content.find('link').text.strip(), headers=headers[random.randint(0,5)])
    soup = bs(nxtPageRes.content, parser='html.parser', features="lxml")
    
    description = [c.text for c in soup.find_all('p')[6:8]]
    
    temp_dict = {
        'title '+str(i): content.find('title').text.strip(),
        'link': content.find('link').text.strip(),
        'subTitle':  content.find('description').text.strip(),
        'pubDate':  content.find('pubDate').text.strip(),
        'desc':  description,
        }
    items.append(temp_dict)
json_items = json.dumps(items)
print(json_items)



    

    












# items = {}
# for i in range(2):
#     items['title'+ str(i)] = contents[i].title.text.strip()
#     items['link'+ str(i)] = contents[i].link.text.strip()
#     items['description'+ str(i)] = contents[i].description.text.strip()

#     res = requests.get(items['link'+ str(i)], headers=header)
#     soup = bs(res.content, features='lxml')
#     id_cnt = items['link'+ str(i)].split('article')
#     id_cnt = id_cnt[1].replace('.ece','')
#     id_cnt = 'content-body-14269002-' + id_cnt

#     for data in soup.findAll('div',{'id':id_cnt}):
#         items['content'+ str(i)] = data.text.strip()

#     # print(items)
# print('Writing to file....')
# # Append-adds at last
# file1 = open("myfile.txt","a")#append mode
# file1.write(f">>{str(items['title0'])}\n>>{str(items['description0'])}\n {str(items['content0'])}\n\n>>{str(items['title1'])}\n>>{str(items['description1'])}\n {str(items['content1'])}\n\nDaily Vocabs:\n")
# # combining both article into single string
# scrapped_content = str(items['content0']) + str(items['content1'])

















# print('Finding Vocabs...')
# # ------getting and searching hard word meanings-------
# result = word_searching(get_string=scrapped_content)
# i = 0
# for key, value in result.items():
#     i+=1
#     file1.write(f'{i}. {key.upper()}---> {value}\n')
  
# file1.close()
# #------------- PDF printing-------------


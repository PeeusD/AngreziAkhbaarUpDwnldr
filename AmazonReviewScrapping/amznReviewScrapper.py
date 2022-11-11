from bs4 import BeautifulSoup 
import requests
from random import randint
import pandas as pd

lastPage = input("Please give your last page number to scrap: ")

for pageNumber in range(1, lastPage+1):
    url = f'https://www.amazon.in/Samsung-Galaxy-Storage-6000mAh-Battery/product-review/B0B4F2TTTS/ref=cm_cr_arp_d_paging_btm_next_2?pageNumber={str(pageNumber)}'

    headers = [{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'},
            { 'User-Agent' :'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'},
                                { 'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'},
                                { 'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'},
                                { 'User-Agent' :'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'},
                                { 'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}]

    res = requests.get(url, headers=headers[randint(0,4)])

    soup = BeautifulSoup(res.text, 'html.parser')
    rev = []
    # all_reviews = soup.find_all('div', {'class':'a-section review aok-relative'})
    all_reviews = soup.findAll('div', {'data-hook':'review'})
    review = {}
    i=0
    for r in all_reviews:
        # print(r)
        # print("-------------------")
        
        review.update({
            'namePerson'+str(i): r.find('span', class_="a-profile-name").text.strip(),
            'reviewTitle'+str(i) : r.find('a', class_="review-title").text.strip(),
            'Rating'+str(i) : r.find('i', {"data-hook":"review-star-rating"}).text.strip(),
            'Ratingdate'+str(i) : r.find('span', {"data-hook":"review-date"}).text.strip(),
            'reviewBody'+str(i) : r.find('span', {"data-hook":"review-body"}).text.strip()
        })
        
        i+=1
print(review)


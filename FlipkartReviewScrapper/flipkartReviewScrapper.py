from bs4 import BeautifulSoup
import time,random
import requests

lastPageNum = int(input("Please enter the last page number: "))
for pageNumber in range(1, lastPageNum+1):
	URL = f"https://www.flipkart.com/samsung-galaxy-m13-midnight-blue-64-gb/product-reviews/itme9d85574c16d5?pid=MOBGGHC2BA4ZN3S5&lid=LSTMOBGGHC2BA4ZN3S5GKBKO5&marketplace=FLIPKART&page={pageNumber}"

	headers = [{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'},
            { 'User-Agent' :'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'},
                                { 'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'},
                                { 'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'},
                                { 'User-Agent' :'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'},
                                { 'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}]


	webpage = requests.get(URL, headers=headers[random.randint(0,5)])
	soup = BeautifulSoup(webpage.content, "html.parser")

	all_content = soup.select(".K0kLPL")
	reviews={}
	i=1
	for c in all_content:
		reviews.update({
			'review-person'+str(i): c.find('p', class_='_2sc7ZR').text.strip(),
			'review-title'+str(i): c.find('p', class_='_2-N8zT').text.strip(),
			'reviewContent'+str(i): c.find('div', class_='t-ZTKy').text.replace("READ MORE","").strip(),
		})
		i+=1
	time.sleep(random.randint(5,15))
	print("pagenumber",pageNumber, ">>completed")

print(reviews)
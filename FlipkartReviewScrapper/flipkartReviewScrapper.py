from bs4 import BeautifulSoup
import time,random
import requests

for pageNumber in range(1,6):
	URL = f"https://www.flipkart.com/samsung-galaxy-m13-midnight-blue-64-gb/product-reviews/itme9d85574c16d5?pid=MOBGGHC2BA4ZN3S5&lid=LSTMOBGGHC2BA4ZN3S5GKBKO5&marketplace=FLIPKART&page={pageNumber}"

	HEADERS =  {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36' }

	webpage = requests.get(URL, headers=HEADERS)
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
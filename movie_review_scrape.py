import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.imdb.com/title/tt7784604/reviews?ref_=tt_urv'

#open connection and grab page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parse
page_soup = soup(page_html, "html.parser")

#grabs each search result
containers = page_soup.findAll("div",{"class":"lister-item-content"})

filename = "reviews.csv"
f = open(filename, "w")
headers = "rating, review"

for container in containers:

	review_container = container.findAll("div",{"class":"text show-more__control"})
	review = review_container[0].text


	text = container.findAll(text=True)
	score = text[8]

	print("score: " + score)
	print("review: " + review + "\n")

	f.write(score + "," + review +"\n")

f.close()




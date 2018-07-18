import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#target webpage
my_url = 'https://www.imdb.com/title/tt7784604/reviews?ref_=tt_urv'

#open connection and grab page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parse
page_soup = soup(page_html, "html.parser")

#grabs each search result
containers = page_soup.findAll("div",{"class":"lister-item-content"})

#file for written reviews
filename_reviews = "scrape\\reviews.txt"
f_scores = open(filename_reviews, "w")

#file for scores/10
filename_scores = "scrape\scores.txt"
f_reviews = open(filename_scores, "w")

#counter =1 

for container in containers:

	#written review container
	review_container = container.findAll("div",{"class":"text show-more__control"})
	review = review_container[0].text

	#score/10 container
	text = container.findAll(text=True)
	score = text[8]

	#write results to corresponding files
	if (score != "\n"):
		f_scores.write(score + "\n")
		f_reviews.write(review + "\n" + "**" + "\n")
		#print(str(counter) + "score: " + score)
		#print(str(counter) + "review: " + review + "\n")
		#counter += 1

#close files
f_scores.close()
f_reviews.close()




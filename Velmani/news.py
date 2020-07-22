import requests

def newsfrombbc():
	url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=8e28348d83544734a0bc5e5187051b3e"

	#fetching api from json format
	open = requests.get(url).json()

	#getting all articles in a string article
	article = open["articles"]

	#empty list which will contain all tending news
	results = []

	for ar in article:
		results.append(ar["title"])


		for i in range(len(results)):
			#printing all trending news
			print(i+1,results[i])
if __name__=='__main__':
	newsfrombbc()


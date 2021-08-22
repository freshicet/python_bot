# importing requests package
import requests	
from decouple import config
def NewsFromAPI():
	
	# BBC news api
	# following query parameters are used
	# source, sortBy and apiKey
	query_params = {
	"source": "the-verge,the-wall-street-journal,fox-news,politico,usa-today,al-jazeera-english,nbc-news,business-insider",
	"sortBy": "top",
	"apiKey": config('apiKey'),
    "q": "security",
    "q": "Hacker"
	}
	main_url = " https://newsapi.org/v2/top-headlines"

	# fetching data in json format
	res = requests.get(main_url, params=query_params)
	open_bbc_page = res.json()

	# getting all articles in a string article
	article = open_bbc_page["articles"]

	# empty list which will
	# contain all trending news
	  #print(article[0]["title"])
    
	title = (article[0]["title"])
	url = (article[0]["url"])
	#print (url)
	#print (title)
	#results = []
	#for ar in article:
	#	#results.append(ar["source"])
	#	print (ar["url"])
	#	
	#for i in range(len(results)):
	#	
	#	# printing all trending news
	#	print(i + 1, results[i])
	return title,url

# function call
NewsFromAPI()

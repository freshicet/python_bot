# importing requests package
import requests	
from decouple import config
def NewsFromAPI():
	
	# News api
	# following query parameters are used
	# source, sortBy and apiKey
	query_params = {
	"source": "the-verge,the-wall-street-journal,fox-news,politico,usa-today,al-jazeera-english,nbc-news,business-insider",
	"sortBy": "top",
	"apiKey": config('apiKey'),
    "q": "security",
    "q": "computer"
	}
	main_url = " https://newsapi.org/v2/top-headlines"

	# fetching data in json format
	res = requests.get(main_url, params=query_params)
	open_page = res.json()

	# getting all articles in a string article
	article = open_page["articles"]

	title = (article[0]["title"])
	url = (article[0]["url"])

	return title,url

# function call
NewsFromAPI()

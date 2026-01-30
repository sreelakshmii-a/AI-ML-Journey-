#api key is not working
#pip install requests
import requests
query=input("What topic is in your head?")
API="pub_cdaadca264d74f6295629fb74c4727e1"



url = f" https://newsdata.io/api/1/latest?apikey={API}&q={query}"


print(url)
r= requests.get(url)
data=r.json()
#articles is a list of dictionary
articles = data["articles"]
for article in articles:
  print(article["title"], article["url"])# "" is the key of dict
  
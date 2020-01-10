import requests
response=requests.get("https://newsapi.org/v2/everything?q=bitcoin&from=2019-12-09&sortBy=publishedAt&apiKey=bd193a7673dd45648370f197f90e4ece")
content=response.json()
art=content['articles']
news1=art[0]
print(news1['title'])

  

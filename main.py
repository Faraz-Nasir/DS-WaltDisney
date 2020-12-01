import requests
from bs4 import BeautifulSoup as bs

res=requests.get("https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films")
b=bs(res.text,'html.parser')

print(b)
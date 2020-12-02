import requests
from bs4 import BeautifulSoup as bs

res=requests.get("https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films")
b=bs(res.text,'html.parser')
link_sub='https://en.wikipedia.org/'
links=[]
tables=b.find_all('table')

for j in range(1,9):
    tbody=tables[j].find('tbody')

    l=tbody.find_all('tr')
    for x in range(1,len(l)):
        link=l[x].find('a')
        if link==None:
            continue
        else:
            links.append(link_sub+link['href'])
print(links)








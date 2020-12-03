import requests
from bs4 import BeautifulSoup as bs

res=requests.get("https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films")
b=bs(res.text,'html.parser')
link_sub='https://en.wikipedia.org/'
links=[]
tables=b.find_all('table')

for j in range(1,10):
    tbody=tables[j].find('tbody')

    l=tbody.find_all('tr')
    for x in range(1,len(l)):
        link=l[x].find('a')
        if link==None:
            continue
        else:
            links.append(link_sub+link['href'])


def checklist(text):
    if(text.td.li):
        list_items=text.td.find_all('li')
        list=[]
        for i in range(len(list_items)):
            list=list_items[i].text.replace("\xa0"," ")
        return list
    elif(text.td.div):
        return text.td.text
    else:
        return text.td.text
# Saving in Json File

import json

def save_data(title,data):
    with open(title,'w',encoding='utf-8') as f:
        json.dump(data,f,ensure_ascii=False,indent=2)

def load_data(title):
    with open(title,encoding='utf-8') as f:
        return json.loads(f)
li_movies=[]
wiki_errors=['This article needs additional citations for verification. Please help improve this article by adding citations to reliable sources. Unsourced material may be challenged and removed.',
             'This article possibly contains original research. Please improve it by verifying the claims made and adding inline citations.',
             'This article has multiple issues. Please help improve it or discuss these issues on the talk page.',
             "This article's tone or style may not reflect the encyclopedic tone used on Wikipedia. See Wikipedia's guide to writing better articles for suggestions.",
             "This article may need to be rewritten to comply with Wikipedia's quality standards. You can help. The talk page may contain suggestions.",
             'This article does not cite any sources. Please help improve this article by adding citations to reliable sources.',
             "This article is missing information about the film's production. Please expand the article to include this information. Further details may exist on the talk page."
             ]
for k in range(len(links)):
    print(k)
    res=requests.get(links[k])
    b=bs(res.text,'html.parser')
    dictonary = {}
    tbody=b.find('tbody')
    tbody=tbody.find_all('tr')
    count=0
    for s in range(len(wiki_errors)):
        try:
            if (wiki_errors[s] in tbody[0].text):
                count+=1
        except AttributeError:
            continue
    if(count==0):
        for t in range(len(tbody)):
            try:
                if t==0:
                    dictonary['title']=tbody[t].text
                elif t==1:
                    continue
                else:
                    Key = tbody[t].th.text
                    Data=checklist(tbody[t])
                    dictonary[Key]=Data

            except AttributeError:
                continue
        print(dictonary)
        li_movies.append(dictonary)
print(len(li_movies))
for i in range(len(li_movies)):
    print(li_movies[i])

save_data("Walt_Disney_Movies.json",li_movies)



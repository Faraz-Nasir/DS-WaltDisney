import requests
from bs4 import BeautifulSoup as bs

def checklist(text):
    if(text.td.li):
        list_items=text.td.find_all('li')
        list=[]
        for i in range(len(list_items)):
            list.append(list_items[i].text)
        return list
    elif(text.td.div):
        return text.td.text
    else:
        return text.td.text

res=requests.get('https://en.wikipedia.org/wiki/Toy_Story_3')
b=bs(res.text,'html.parser')

tbody=b.find('tbody')
tbody=tbody.find_all('tr')
dictonary={}

for i in range(len(tbody)):
    if i==0:
        dictonary['title']=tbody[i].text
    elif i==1:
        continue

    elif i==12:
        list=checklist(tbody[i])
        list_confirmed=[]
        for i in range(len(list)):
            list_confirmed.append(bs(list[i],'html.parser'))
        Key = tbody[i].get_text()
        Data = list_confirmed
        dictonary[Key] = Data
    elif i==16 or i==17:
        list = checklist(tbody[i])
        list=bs(list,'html.parser')
        Key = tbody[i].th.text
        Data = list
        dictonary[Key] = Data
    else:
        Key=tbody[i].th.text
        Data=checklist(tbody[i])
        dictonary[Key]=Data

print(dictonary)
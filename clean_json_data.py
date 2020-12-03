import json
def load_data(title):
    with open(title,encoding='utf-8') as f:
        return json.load(f)
def save_data(title,text):
    with open(title,'w',encoding='utf-8') as f:
        json.dump(text,f,ensure_ascii=False,indent=2)

dict=load_data("Walt_Disney_Movies.json")


#Convert time into an integer
#Convert dates to datetimeobject
#convert budget and box office into numbers
#clean up refernces [1][2]

edit_list=["1","2","3","4","5","6","7","8","9","10",]

#removes [1] etc and "\xa0" from all values in dict
"""for i in range(len(dict)):
    list = []
    for key in dict[i].keys():
        list.append(key)
    for s in list:
        for j in range(len(edit_list)):
            if('['+edit_list[j]+ ']' in dict[i][s]):
                dict[i][s]=dict[i][s].replace("["+edit_list[j]+"]","")
            if("\xa0" in dict[i][s]):
                dict[i][s] = dict[i][s].replace("\xa0", "")
for i in range(len(dict)):
    print(dict[i])


save_data("Walt_Disney_Movies.json",dict)"""
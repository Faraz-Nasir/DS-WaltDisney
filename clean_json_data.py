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
#clean up refernces [1][2](Done)

"""
count=0
for i in range(len(dict)):
    list=[]
    list_keys=[]
    for values in dict[i].values():
        list.append(values)
    for keys in dict[i].keys():
        list_keys.append(keys)

    for j in range(len(list)):
        if('minutes' in list[j]):
            if('Running time' in list_keys[j]):
                count+=1
                continue
            else:
                print(list_keys[j])

print(count)
print(len(dict))"""

#removes [1] etc and "\xa0" from all values in dict
"""
edit_list=["1","2","3","4","5","6","7","8","9","10"]
for i in range(len(dict)):
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

"""#minutes,min,list
def minute_to_integer(running_time):
    value=running_time.split(" ")[0]
    return value
minutes=[value.get("Running time","N/A") for value in dict]
mins=[]#removed minutes word from list(minutes)
for i in minutes:
    mins.append(minute_to_integer(i))
for i in range(len(mins)):
    if('minutes' in mins[i]):
        mins[i]=mins[i].replace("minutes","")
        mins[i]=int(mins[i])
    else:
        mins[i]=mins[i]


for i in range(len(mins)):
    if(mins[i]!='N/A'):
        dict[i]["Running time"]=mins[i]
    else:
        continue

for i in range(len(dict)):
    try:
        if("Running time" in dict[i]):
            dict[i]["Running time"]=int(mins[i])
    except:
        dict[i]["Running time"]=23
        print("Done")

save_data("Walt_Disney_Movies.json",dict)
"""
"""dict=load_data("Walt_Disney_Movies.json")
for i in range(len(dict)):
    keys=dict[i].keys()
    if("Budget" in keys):
        if "." in dict[i]["Budget"]:
            dict[i]["Budget"] = dict[i]["Budget"].replace(".", "")
        if "$" in dict[i]["Budget"]:
            dict[i]["Budget"] = dict[i]["Budget"].replace("$", "")
        if "million" in dict[i]["Budget"]:
            dict[i]["Budget"]=dict[i]["Budget"].replace(" million","000000")
            dict[i]["Budget"] = dict[i]["Budget"].replace("million", "000000")
        if "billion" in dict[i]["Budget"]:
            dict[i]["Budget"]=dict[i]["Budget"].replace(" billion","000000000")
            dict[i]["Budget"] = dict[i]["Budget"].replace("billion", "000000000")
    if("Box office" in keys):
        if "." in dict[i]["Box office"]:
            dict[i]["Box office"] = dict[i]["Box office"].replace(".", "")
        if "$" in dict[i]["Box office"]:
            dict[i]["Box office"] = dict[i]["Box office"].replace("$", "")
        if "million" in dict[i]["Box office"]:
            dict[i]["Box office"]=dict[i]["Box office"].replace(" million","000000")
            dict[i]["Box office"] = dict[i]["Box office"].replace("million", "000000")
        if "billion" in dict[i]["Box office"]:
            dict[i]["Box office"]=dict[i]["Box office"].replace(" billion","000000000")
            dict[i]["Box office"] = dict[i]["Box office"].replace("billion", "000000000")
save_data("Walt_Disney_Movies.json",dict)
"""
#save data using pickle
import pickle
def save_data_pickle(pickle_doc,pass_dictonary):
    with open(pickle_doc,"wb") as f:
        pickle.dump(pass_dictonary,f)

def load_data_pickle(pickle_doc):
    with open(pickle_doc,"rb") as f:
        return pickle.load(f)

save_data_pickle("Walt_Disney_Movie_Pickle.pickle",dict)
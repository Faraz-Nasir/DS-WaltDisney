import json
def load_data(title):
    with open(title,encoding='utf-8') as f:
        return json.dumps(f)

print(load_data("Walt_Disney_Movies.json"))

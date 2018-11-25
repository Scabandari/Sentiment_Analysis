import requests
import json

def make_req(sentiment):
    token ="my token"
    url = "https://sleepy-lake-52420.herokuapp.com/api/twitter/5bef243462a7de634e0bb5c5"

    data={"sentiment":str(sentiment)}
    headers = {
    'Authorization': 'Bearer ' + token, "Content-Type": "application/json"
    }
    response = requests.put(url,data=json.dumps(data), headers=headers)

read_lines = []

with open("score.txt", 'r') as f:
    for line in f:
        read_lines.append(line)

make_req(read_lines[-1])



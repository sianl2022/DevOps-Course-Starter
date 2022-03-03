import requests
import dontenv
import os


def mark_card_done(card_id):
    params = {
        'idList': idList,
        'key' : os.getenv('TRELLO_KEY'),
        'token' : os.getenv('TRELLO_TOKEN') 
    }
    requests.post('https://api.trello.com/1/cards/', params=params)

def create_card(idList, name):
    params = {
        'idList' : idList,
        'name' : name,
        'key' : os.getenv('TRELLO_KEY'),
        'token' : os.getenv('TRELLO_TOKEN')
    }
    request.post('https://api.trello.com/1/cards/{card_id}', params=params)



url = "https://api.trello.com/1/boards/AbpSrXDQ/lists"

env_file = dotenv.load_dotenv(".env")

os.getenv("TRELLO_API_KEY")

querystring = {
"key":os.getenv("TRELLO_API_KEY"),
"token":os.getenv("TRELLO_API_TOKEN"),
"cards":"open"
}

response = requests.request("GET", url, params=querystring)

print(response.text)
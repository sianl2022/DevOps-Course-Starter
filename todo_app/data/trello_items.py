import requests
import os
from todo_app.data.item import Item

def get_items():
    url = "https://api.trello.com/1/boards/AbpSrXDQ/lists"

    querystring = {
    "key":os.getenv("TRELLO_API_KEY"),
    "token":os.getenv("TRELLO_API_TOKEN"),
    "cards": "open" }

    response = requests.request("GET", url, params=querystring)

    response_json = response.json()

    items = []

    for trello_list in response_json:
        for card in trello_list['cards']:
            card['status'] = trello_list['name']
            item = Item(card['id'], card['name'], card['status'])
            items.append(item)

    return items

def complete_card(card_id):
    params = {
        'idList': "620d07e38fa8a1448485d3f7",
        'key' : os.getenv('TRELLO_API_KEY'),
        'token' : os.getenv('TRELLO_API_TOKEN') 
    }
    response = requests.put(f'https://api.trello.com/1/cards/{card_id}', params=params)

    response.raise_for_status()

def create_card(name):
    params = {
        'idList' : "620d07e38fa8a1448485d3f5",
        'name' : name,
        'key' : os.getenv('TRELLO_API_KEY'),
        'token' : os.getenv('TRELLO_API_TOKEN')
    }
    response = requests.post('https://api.trello.com/1/cards', params=params)

    response.raise_for_status()




import requests
import os


def mark_card_done(card_id):
    params = {
        'idList': "62d07e38fa8a1448485d3f7",
        'key' : os.getenv('TRELLO_API_KEY'),
        'token' : os.getenv('TRELLO_API_TOKEN') 
    }
    requests.post('https://api.trello.com/1/cards/', params=params)

def create_card(name):
    params = {
        'idList' : "620d07e38fa8a1448485d3f5",
        'name' : name,
        'key' : os.getenv('TRELLO_API_KEY'),
        'token' : os.getenv('TRELLO_API_TOKEN')
    }
    response = requests.post('https://api.trello.com/1/cards', params=params)

    response.raise_for_status()




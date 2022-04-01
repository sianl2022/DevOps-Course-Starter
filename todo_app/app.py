from flask import Flask, render_template, request
from todo_app.data.session_items import add_item, get_items
from todo_app.data.trello_items import create_card

from todo_app.flask_config import Config
import requests
import os

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():

    url = "https://api.trello.com/1/boards/AbpSrXDQ/lists"

    os.getenv("TRELLO_API_KEY")

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
            items.append(card)

    return render_template('index.html', items = items)

@app.route('/create-a-todo', methods=['POST'])
def create_new_todo():
    new_todo_title = request.form['todo-name']
    create_card(new_todo_title)
    return index()
    

@app.route('/move-to-done', methods=['POST'])
def mark_card_done(card_id):
    params = {
        'idList': '62d07e38fa8a1448485d3f7',
        'key' : os.getenv('TRELLO_API_KEY'),
        'token' : os.getenv('TRELLO_API_TOKEN') 
    }
    requests.post('https://api.trello.com/1/cards/', params=params)
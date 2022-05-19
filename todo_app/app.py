from flask import Flask, render_template, request
from todo_app.data.trello_items import create_card, complete_card, get_items

from todo_app.flask_config import Config
import requests
import os

app = Flask(__name__)
app.config.from_object(Config())

class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', items = items)

@app.route('/create-a-todo', methods=['POST'])
def create_new_todo():
    new_todo_title = request.form['todo-name']
    create_card(new_todo_title)
    return index()
    

@app.route('/move-to-done/<card_id>', methods=['POST'])
def mark_card_done(card_id):
    complete_card(card_id)
    return index()
from flask import Flask, render_template, request
from todo_app.data.trello_items import create_card, complete_card, get_items

from todo_app.flask_config import Config
from todo_app.templates.view_model import ViewModel
import requests
import os

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    items = get_items()
    item_view_model = ViewModel(items)
    return render_template('index.html', view_model=item_view_model)

@app.route('/create-a-todo', methods=['POST'])
def create_new_todo():
    new_todo_title = request.form['todo-name']
    create_card(new_todo_title)
    return index()
    

@app.route('/move-to-done/<card_id>', methods=['POST'])
def mark_card_done(card_id):
    complete_card(card_id)
    return index()
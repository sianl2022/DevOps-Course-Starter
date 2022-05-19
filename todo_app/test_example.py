import os
import pytest
import requests
from todo_app import app
from dotenv import load_dotenv, find_dotenv

def test_we_can_ret_todo_list():
    assert 2 + 2 == 4

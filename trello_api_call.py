import requests
import dontenv
import os

url = "https://api.trello.com/1/members/me/boards"

env_file = dotenv.load_dotenv(".env")

os.getenv("TRELLO_API_KEY")

querystring = {"key":os.getenv("TRELLO_API_KEY"),"token":os.getenv("TRELLO_API_TOKEN")}

response = requests.request("GET", url, params=querystring)

print(response.text)
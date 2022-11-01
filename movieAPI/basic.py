import requests

endpoint = "http://localhost:8000/movies"

get_response = requests.get(endpoint + "/2019")

print(get_response.json())
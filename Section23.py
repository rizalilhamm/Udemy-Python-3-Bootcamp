""" Python request """
import requests

url = 'https://icanhazdadjoke.com/'

respone = requests.get(url, headers={'Accept': 'application/json'})

# print(respone.text)
# print(type(respone.text))
# print(respone.json())
# print(type(respone.json()))

data = respone.json()
print(type(data))
print(f"Joke  : {data['joke']}")
print(f"Status: {data['status']}")
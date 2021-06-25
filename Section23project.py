import requests
from random import choice, choices
from pyfiglet import figlet_format
from termcolor import colored

header = figlet_format("DAD JOKES 3000!")
header = colored(header, color='white')
print(header)

user_input = input("What wold you like to search for? ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params = {"term": user_input}
    ).json()

num_jokes = res['total_jokes']
results = res['results']
if num_jokes > 1:
    print(f"I found {num_jokes} jokes about {user_input} Here's one: ")
    print(choice(results)['joke'])
    print("THERE ARE MANY JOKES")
elif num_jokes == 1:
    print(res['results'][0])
    print("THERE ARE ONLY ONE JOKE")
else:
    print(f"Sorry we can not find jokes with your term: {user_input}")
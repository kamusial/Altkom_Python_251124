import requests
from bs4 import BeautifulSoup

url = 'https://allegro.pl'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.prettify())
print(soup.title.text)
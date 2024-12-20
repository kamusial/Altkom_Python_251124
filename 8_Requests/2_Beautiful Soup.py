from bs4 import BeautifulSoup
import requests

html = """
<html>
  <head><title>Przykładowa strona</title></head>
  <body>
    <h1 id="main-header">Nagłówek</h1>
    <p class="description">To jest przykładowy paragraf.</p>
    <a href="https://example.com" class="link">Odwiedź stronę</a>
    <a href="https://allegro.com" class="link">Odwiedź stronę</a>
  </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

# print(soup)
# print(soup.prettify())
print(soup.title.text)
print(soup.find('h1').text)
print(soup.find('a')['href'])

links =soup.find_all('a')
for link in links:
    print(link['href'])

description = soup.find('p', class_ ='description')
print(description.text)

link = soup.find('a', {'class': "link"})
print(link['href'])
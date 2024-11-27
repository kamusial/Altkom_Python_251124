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

print(soup.html.head.title.text)

header = soup.find('h1')
print(header.find_next_sibling('p').text)

header.string = 'Zmieniony nagłówek'
print(header)
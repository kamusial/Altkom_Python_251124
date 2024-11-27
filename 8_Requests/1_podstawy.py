import requests

# response = requests.get('https://simple-books-api.glitch.me/status')
# print(response.status_code)
# print(response.text)

page = 'https://simple-books-api.glitch.me/api-clients/'
data = {
    'clientName': 'Kamil',
    'clientEmail': '1123@w4390erww5w.pl'
}
response = requests.post(page, json=data)
print(response.status_code)
print(response.json())
token = response.json()['accessToken']

page = 'https://simple-books-api.glitch.me/orders/'
data = {
  "bookId": 1,
  "customerName": "Kamil"
}
response = requests.post(page, json=data, headers={'Authorization': token})
print(response.status_code)
print(response.json())

response = requests.get('https://simple-books-api.glitch.me/orders/'+str(response.json()['orderId']), headers={'Authorization': token})
print(response.status_code)
print(response.text)
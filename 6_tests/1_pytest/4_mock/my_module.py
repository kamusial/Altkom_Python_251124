import requests

def get_user_data(user_id):
    response = requests.get('http://example/users/{}'.format(user_id))
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError('User not found')


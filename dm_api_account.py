import requests

def post_v1_account():
    headers = {
        'accept': '*/*',
        'Content-Type': 'application/json',
    }

    json_data = {
        'login': 'new_user2',
        'email': 'new_user2@mail.ru',
        'password': 'new_user2',
    }

    response = requests.post('http://localhost:5051/v1/account', headers=headers, json=json_data)
    return response

# print(post_v1_account())

def put_v1_account_token(token):
    headers = {
        'accept': 'text/plain',
    }
    response = requests.put(f'http://localhost:5051/v1/account/{token}', headers=headers)
    return response

print(put_v1_account_token(token='5c42b20b-900d-48e8-8dd1-0371bc5c71e5'))

def post_v1_account_login(login, password, remember_me=True):
    headers = {
        'accept': 'text/plain',
        'Content-Type': 'application/json',
    }

    json_data = {
        'login': login,
        'password': password,
        'rememberMe': remember_me,
    }

    response = requests.post('http://localhost:5051/v1/account/login', headers=headers, json=json_data)
    return response

response = post_v1_account_login(
    login='new_user2',
    password='new_user2'
)

print(response.json())
print(response.headers['X-Dm-Auth-Token'])
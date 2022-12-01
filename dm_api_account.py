import requests
import random
import mailhog

def post_v1_account(login, email, password):
    headers = {
        'accept': '*/*',
        'Content-Type': 'application/json',
    }

    json_data = {
        'login': login,
        'email': email,
        'password': password,
    }

    response = requests.post('http://localhost:5051/v1/account', headers=headers, json=json_data)
    return response

def get_v1_account(token):
    headers = {
        'accept': 'text/plain',
        'X-Dm-Auth-Token': token,
    }

    response = requests.get('http://localhost:5051/v1/account', headers=headers)
    return response


def put_v1_account_token(token):
    headers = {
        'accept': 'text/plain',
    }
    response = requests.put(f'http://localhost:5051/v1/account/{token}', headers=headers)
    return response

def post_v1_account_password(login, email):
    headers = {
        'accept': 'text/plain',
        'Content-Type': 'application/json',
    }
    json_data = {
        'login': login,
        'email': email,
    }
    return requests.post('http://localhost:5051/v1/account/password', headers=headers, json=json_data)


def put_v1_account_password(login, reset_token, old_password, new_password):
    headers = {
        'accept': 'text/plain',
        'Content-Type': 'application/json',
    }

    json_data = {
        'login': login,
        'token': reset_token,
        'oldPassword': old_password,
        'newPassword': new_password,
    }

    return requests.put('http://localhost:5051/v1/account/password', headers=headers, json=json_data)



def put_v1_account_email(login, password, email):
    headers = {
        'accept': 'text/plain',
        'Content-Type': 'application/json',
    }

    json_data = {
        'login': login,
        'password': password,
        'email': email,
    }

    return requests.put('http://localhost:5051/v1/account/email', headers=headers, json=json_data)





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
    print(response.json())
    auth_token = response.headers['X-Dm-Auth-Token']
    return auth_token

def delete_v1_account_login(token):
    headers = {
        'accept': 'text/plain',
        'X-Dm-Auth-Token': token,
    }

    return requests.delete('http://localhost:5051/v1/account/login', headers=headers)
def delete_v1_account_login_all(token):
    headers = {
        'accept': 'text/plain',
        'X-Dm-Auth-Token': token,
    }

    return requests.delete('http://localhost:5051/v1/account/login/all', headers=headers)



rnd = random.randint(0, 50000)
login = f'new_user{rnd}'
email = f'new_user{rnd}@email.ru'
password = login
print(0, login, email, password)
print(1, post_v1_account(login, email, password))
activation_token = mailhog.post_v2_messages()
print(2, activation_token)
print(3, put_v1_account_token(token=activation_token))

auth_token = post_v1_account_login(
    login=login,
    password=password
)

# print(response.json())
print(4, auth_token)

print(5, get_v1_account(token=auth_token).json())
print(6, post_v1_account_password(login, email))
reset_token = mailhog.post_v2_messages()
print(7, reset_token)
new_password = password + '1'
print(8, put_v1_account_password(login, reset_token, password, new_password).json())
# auth_token = post_v1_account_login(
#     login=login,
#     password=new_password # password
# )
# print(auth_token)
new_email = '1' + email
print(new_email)
print(9, put_v1_account_email(login, new_password, new_email).json())
confirm_token = mailhog.post_v2_messages()
print(confirm_token)
print(10, put_v1_account_token(token=confirm_token))
print(11, delete_v1_account_login(auth_token))
print(12, get_v1_account(token=auth_token).json())
auth_token1 = post_v1_account_login(
    login=login,
    password=new_password
)
auth_token2 = post_v1_account_login(
    login=login,
    password=new_password
)
auth_token3 = post_v1_account_login(
    login=login,
    password=new_password
)
print(auth_token1, auth_token2 ,auth_token3)
print(13, delete_v1_account_login_all(auth_token1))

print(14, get_v1_account(token=auth_token1).json())
print(15, get_v1_account(token=auth_token2).json())
print(16, get_v1_account(token=auth_token3).json())


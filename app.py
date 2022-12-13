import structlog

from dm_api_account.account_api import AccountApi
from dm_api_account.login_api import LoginApi
from dm_api_account.mailhog_api import MailHogApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)
login = LoginApi(host='http://localhost:5051')
account = AccountApi(host='http://localhost:5051')
mailhog = MailHogApi(host='http://localhost:5025')

login_credentials = {
    'login': 'new_user3',
    'password': 'new_user3',
    'rememberMe': True,
}
response = login.post_v1_account_login(login_credentials=login_credentials)
print(response.headers['X-Dm-Auth-Token'])

headers = {
    'X-Dm-Auth-Token': response.headers['X-Dm-Auth-Token']
}
response = account.get_v1_account(headers=headers, params=None)
print(response.json())

response = mailhog.get_v2_messages('50')
print(response)

response = mailhog.delete_v2_messages()
print(response)

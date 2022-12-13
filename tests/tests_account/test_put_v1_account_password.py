import datetime
import time

import structlog

from dm_api_account.account_api import AccountApi
from dm_api_account.login_api import LoginApi
from dm_api_account.mailhog_api import MailHogApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)

class TestsPutV1AccountPassword:
    def test_put_v1_account_password(self):
        login = LoginApi(host='http://localhost:5051')
        login_credentials = {
            'login': 'new_user3',
            'password': 'new_user3',
            'rememberMe': True,
        }
        response1 = login.post_v1_account_login(login_credentials=login_credentials)

        account = AccountApi(host='http://localhost:5051')
        change_password_model = {
            'login': 'new_user3',
            'token': response1.headers['X-Dm-Auth-Token'],
            'oldPassword': 'new_user3',
            'newPassword': 'new_user33',
        }
        response = account.put_v1_account_password(change_password_model)
        print(change_password_model, response.text)
        assert response.status_code == 200, f"Статус код ответа должен быть 200, но он равен {response.status_code}"
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
        mail = MailHogApi(host='http://localhost:5025')
        activation_token = mail.get_token_from_last_email()
        account = AccountApi(host='http://localhost:5051')
        change_password_model = {
            'login': 'login12',
            'token': activation_token,
            'oldPassword': 'star123',
            'newPassword': 'star1234',
        }
        response = account.put_v1_account_password(change_password_model)
        print(change_password_model, response.text)
        assert response.status_code == 200, f"Статус код ответа должен быть 200, но он равен {response.status_code}"
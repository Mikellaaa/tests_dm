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

class TestsPostV1AccountPassword:
    def test_post_v1_account_password(self):
        account = AccountApi(host='http://localhost:5051')
        registration_model = {
            'login': 'loginsasd1',
            'email': f'asdaaaasdasdas1@mail.ru',
            'password': 'password1',
        }
        response = account.post_v1_account(registration_model)
        mail = MailHogApi(host='http://localhost:5025')
        activation_token = mail.get_token_from_last_email()
        response = account.put_v1_account_token(token=activation_token)


        reset_password_model = {
            'login': 'loginsasd1',
            'email': 'asdaaaasdasdas1@mail.ru',
        }
        response = account.post_v1_account_password(reset_password_model)
        assert response.status_code == 200, f"Статус код ответа должен быть 200, но он равен {response.status_code}"
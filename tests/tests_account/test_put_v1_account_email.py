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

class TestsPutV1AccountEmail:
    def test_put_v1_account_email(self):
        account = AccountApi(host='http://localhost:5051')

        response = account.put_v1_account_email(change_password_model)
        print(change_password_model, response.text)
        assert response.status_code == 200, f"Статус код ответа должен быть 200, но он равен {response.status_code}"
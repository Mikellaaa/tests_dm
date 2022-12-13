import structlog

from dm_api_account.account_api import AccountApi
from dm_api_account.login_api import LoginApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)
class TestsGetV1Account:
    def test_get_v1_account(self):
        account = AccountApi(host='http://localhost:5051')
        login = LoginApi(host='http://localhost:5051')
        login_credentials = {
            'login': 'new_user3',
            'password': 'new_user3',
            'rememberMe': True,
        }
        auth_token = login.post_v1_account_login(login_credentials=login_credentials).headers['X-Dm-Auth-Token']

        headers = {
            'X-Dm-Auth-Token': auth_token
        }
        response = account.get_v1_account(headers=headers, params=None)
        assert response.status_code == 200, f"Статус код ответа должен быть 200, но он равен {response.status_code}"
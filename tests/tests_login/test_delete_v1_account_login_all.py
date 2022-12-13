import structlog

from dm_api_account.login_api import LoginApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)

class TestsDeleteV1AccountLogin:

    def test_delete_v1_account_login(self):
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
        response = login.delete_v1_account_login(headers=headers)
        assert response.status_code == 204, f"Статус код ответа должен быть 200, но он равен {response.status_code}"
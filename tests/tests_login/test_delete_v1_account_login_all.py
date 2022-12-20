import structlog

from dm_api_account.login_api import LoginApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)

class TestsDeleteV1AccountLogin:

    def test_delete_v1_account_login(self, login_user):
        response = login_user.delete_v1_account_login()
        assert response.status_code == 204, f"Статус код ответа должен быть 200, но он равен {response.status_code}"
import structlog

from dm_api_account.account_api import AccountApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)

class TestsPostV1Account:
    def test_post_v1_account(self):
        account = AccountApi(host='http://localhost:5051')
        registration_model = {
            'login': 'login',
            'email': 'email@mail.ru',
            'password': 'password',
        }
        response = account.post_v1_account(registration_model)
        assert response.status_code == 201, f"Статус код ответа должен быть 200, но он равен {response.status_code}"
class TestsDeleteV1AccountLogin:
    def test_delete_v1_account_login(self, login_api, user_headers):
        response = login_api.delete_v1_account_login(headers=user_headers)
        print('===========', response.request.headers)
        assert response.status_code == 204, f"Статус код ответа должен быть 200, но он равен {response.status_code}"

    def test_delete_v1_account_login_1(self, login_user):
        response = login_user.delete_v1_account_login()
        print('===========', response.request.headers)
        assert response.status_code == 204, f"Статус код ответа должен быть 200, но он равен {response.status_code}"
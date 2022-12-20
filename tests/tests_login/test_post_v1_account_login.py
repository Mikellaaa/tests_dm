import pytest
from hamcrest import assert_that, has_entries

def check_str_value(value):
    quality = value["rating"]["quality"]
    if not isinstance(quality, str):
        raise AssertionError(f'quality should be str value but value type = {type(quality)}')

class TestsPostV1AccountLogin:
    def test_post_v1_account_login(self, login_api):
        login_credentials = {
            'login': 'new_user3',
            'password': 'new_user3',
            'rememberMe': True,
        }
        response = login_api.post_v1_account_login(login_credentials=login_credentials)
        assert response.status_code == 200, f"Статус код ответа должен быть 200, но он равен {response.status_code}"
        json_ = response.json()["resource"]
        check_str_value(json_)
        assert_that(json_, has_entries(
            {
                "login": "new_user3",
                "rating": {
                    "enabled": True,
                    "quality": 0,
                    "quantity": 0
                },
                "roles": [
                    "Guest",
                    "Player"
                ]
            }
        ))
        # expected_json = {
        #     "resource": {
        #         "login": "new_user3",
        #         # "online": "2022-12-13T12:56:30.207456+00:00",
        #         "rating": {
        #             "enabled": True,
        #             "quality": 0,
        #             "quantity": 0
        #         },
        #         # "registration": "2022-12-06T14:23:11.898673+00:00",
        #         "roles": [
        #             "Guest",
        #             "Player"
        #         ]
        #     }
        # }
        # actual_json = response.json()
        # assert actual_json['resource']['login'] == expected_json['resource']['login']
        # actual_json['resource'].pop("online")
        # actual_json['resource'].pop("registration")
        # assert actual_json == expected_json

    def test_post_v1_account_login_negative(self, login_api):
        login_credentials = {
            'login': 'new_user3',
            'password': 'new_user31',
            'rememberMe': True,
        }
        response = login_api.post_v1_account_login(login_credentials=login_credentials)
        assert response.status_code == 400, f"Статус код ответа должен быть 400, но он равен {response.status_code}"

    @pytest.mark.skip('Нет реализации')
    def test_login_by_unregistered_user(self):
        ...

    @pytest.mark.skip('Нет реализации')
    def test_login_by_registered_user(self):
        ...

    @pytest.mark.skip('Нет реализации')
    def test_login_wrong_password(self):
        ...
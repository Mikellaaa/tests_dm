import requests

login_credentials = {
    'login': 'login',
    'password': 'password',
    'rememberMe': 'remember_me',
}
class LoginApi:
    def __init__(self, host: str = 'http://localhost:5051', headers: dict = None):
        self.host = host
        self.session = requests.session()
        self.session.headers = headers

    def post_v1_account_login(self, login_credentials: dict, **kwargs: dict) -> requests.Response:
        """
        Authenticate via credentials
        :param login_credentials:
        :return:
        """
        response = requests.post(
            url='http://localhost:5051/v1/account/login',
            json=login_credentials,
            **kwargs,
        )
        # print(response.json())
        # auth_token = response.headers['X-Dm-Auth-Token']
        return response

    def delete_v1_account_login(self, token, **kwargs: dict) -> requests.Response:
        """
        Logout as current user
        :return:
        """
        response = requests.delete(
            url='http://localhost:5051/v1/account/login',
            **kwargs,
        )
        return response

    def delete_v1_account_login_all(self, token, **kwargs: dict) -> requests.Response:
        """
        Logout from every device
        :return:
        """
        response = requests.delete(
            url='http://localhost:5051/v1/account/login/all',
            **kwargs,
        )
        return response
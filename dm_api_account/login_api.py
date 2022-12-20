import requests
from utilities.rest_client import RestClient

login_credentials = {
    'login': 'login',
    'password': 'password',
    'rememberMe': 'remember_me',
}

def logger(function):
    def _logger(*args, **kwargs):
        print(function.__name__)
        print(function.__doc__)
        for arg in args:
            print(f"arg: {arg}")
        for key, value in kwargs.items():
            print(f'{key}: {value}')
        response: requests.Response
        response = function(*args, **kwargs)
        print(f"""
        REQUEST
        method {response.request.method}
        method {response.request.url}
        method {response.request.body}
        method {response.request.headers}
        method {response.request.method}
        RESPONSE:
        status_code {response.status_code}
        method {response.content}
        method {response.headers}
        """)
        return response

    return _logger

class LoginApi:
    def __init__(self, host: str = 'http://localhost:5051', headers: dict = None):
        self.host = host
        self.client = RestClient(host=host, headers=headers)
    def set_headers(self, headers):
        self.client.session.headers = headers
    @logger
    def post_v1_account_login(self, login_credentials: dict, **kwargs: dict) -> requests.Response:
        """
        Authenticate via credentials
        :param login_credentials:
        :return:
        """
        response = self.client.post(
            path='/v1/account/login',
            json=login_credentials,
            **kwargs,
        )
        return response

    def delete_v1_account_login(self, **kwargs: dict) -> requests.Response:
        """
        Logout as current user
        :return:
        """
        response = self.client.delete(
            path='/v1/account/login',
            **kwargs,
        )
        return response

    def delete_v1_account_login_all(self, **kwargs: dict) -> requests.Response:
        """
        Logout from every device
        :return:
        """
        response = self.client.delete(
            path='/v1/account/login/all',
            **kwargs,
        )
        return response
import requests

registration_model = {
    'login': 'login',
    'email': 'email',
    'password': 'password',
}

change_password_model = {
    'login': 'login',
    'token': 'reset_token',
    'oldPassword': 'old_password',
    'newPassword': 'new_password',
}

reset_password_model = {
    'login': 'login',
    'email': 'email',
}

change_email = {
    'login': 'login',
    'password': 'password',
    'email': 'email',
}


class AccountApi:
    def __init__(self, host: str = 'http://localhost:5051', headers: dict = None):
        self.host = host
        self.session = requests.session()
        self.session.headers = headers

    def post_v1_account(self, registration_model: dict, **kwargs: dict) -> requests.Response:
        """
        Register new user
        :param registration_model:
        :return:
        """
        response = self.session.post(
            url=f'{self.host}/v1/account',
            json=registration_model,
            **kwargs,
        )
        return response

    def get_v1_account(self, **kwargs: dict):
        """
        Get current user
        :return:
        """
        print(kwargs)
        response = self.session.get(
            url=f'{self.host}/v1/account',
            **kwargs,
        )
        return response

    def put_v1_account_token(self, token: str, **kwargs: dict) -> requests.Response:
        """
        Activate registered user
        :param token: Activation token
        :return:
        """
        response = self.session.put(
            url=f'{self.host}/v1/account/{token}',
            **kwargs,
        )
        return response

    def post_v1_account_password(self, reset_password_model: dict, **kwargs: dict) -> requests.Response:
        """
        Reset registered user password
        :param reset_password_model:
        :return:
        """
        response = self.session.post(
            url=f'{self.host}/v1/account/password',
            json=reset_password_model,
            **kwargs,
        )
        return response

    def put_v1_account_password(self, change_password_model: dict, **kwargs: dict) -> requests.Response:
        """
        Change registered user password
        :param change_password_model:
        :return:
        """
        response = self.session.put(
            url=f'{self.host}/v1/account/password',
            json=change_password_model
            **kwargs,
        )
        return response

    def put_v1_account_email(self, change_email: dict, **kwargs: dict) -> requests.Response:
        """
        Change registered user email
        :param change_email:
        :return:
        """
        response = self.session.put(
            url=f'{self.host}/v1/account/email',
            json=change_email,
            **kwargs,
        )
        return response

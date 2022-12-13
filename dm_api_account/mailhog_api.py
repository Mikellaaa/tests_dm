import requests
from utilities.rest_client import RestClient


class MailHogApi:
    def __init__(self, host: str = 'http://localhost:5025', headers: dict = None):
        self.host = host
        self.session = requests.session()
        self.client = RestClient(host=host, headers=headers)

    def get_token_from_last_email(self) -> str:
        """
        Get token from last email
        :return:
        """
        params = {
            'limit': '1',
        }

        response = self.client.get(
            path='/api/v2/messages',
            params=params,
        )
        json_string = response.json()['items'][0]['Content']['Body']
        activation_token = json_string.split('/')[-1][:-2]

        return activation_token

    def delete_v2_messages(self, **kwargs) -> requests.Response:
        """
        Delete all messages
        :return:
        """
        response = self.client.delete(
            path='/api/v1/messages',
            **kwargs
        )
        return response

    def get_v2_messages(self, limit: str) -> requests.Response:
        """
        Get messages
        :return:
        """
        params = {
            'limit': limit,
        }

        response = self.client.get(
            path='/api/v2/messages',
            params=params,
        )
        # items = response.json()['items']
        return response

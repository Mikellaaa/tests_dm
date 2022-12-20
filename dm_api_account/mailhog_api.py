import json
import time
import requests

from utilities.rest_client import RestClient
from hamcrest import assert_that, has_entries, has_key

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

    def get_v2_messages(self, limit: str) -> list:
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
        messages = []
        items = response.json()['items']
        for item in items:
            json_string = item['Content']['Body']
            value = json.loads(json_string)
            messages.append(value)
        return messages

    def get_token(self, type: str, login) -> requests.Response:
        """
        Get token
        :param type:
        :param login:
        :return:
        """
        messages = self.get_v2_messages('5')
        for message in messages:
            if login == message['Login']:
                if type == 'confirmation' and message.get('ConfirmationLinkUrl'):
                    return message['ConfirmationLinkUrl'].split('/')[-1][:-2]
                if type == 'reset' and message.get['ConfirmationLinkUri']:
                    return message['ConfirmationLinkUri'].split('/')[-1][:-2]
        time.sleep(2)
        return self.get_token(type, login)



login = 'login12222222222'
mail = MailHogApi(host='http://localhost:5025')
activation_token = mail.get_token(login=login, type='confirmation')
print(33333333333333333333, activation_token)


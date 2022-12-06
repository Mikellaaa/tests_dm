import requests


class MailHogApi:
    def __init__(self, host: str = 'http://localhost:5025'):
        self.host = host
        self.session = requests.session()

    def get_last_token_v2_messages(self):
        """
        Get last token
        :return:
        """
        params = {
            'limit': '1',
        }

        response = requests.get(
            url=f'{self.host}api/v2/messages',
            params=params,
        )
        json_string = response.json()['items'][0]['Content']['Body']
        activation_token = json_string.split('/')[-1][:-2]

        return activation_token

    def delete_v2_messages(self):
        """
        Delete all messages
        :return:
        """
        response = requests.delete(
            url=f'{self.host}/api/v1/messages'
        )
        return response

    def get_v2_messages(self):
        """
        Get messages
        :return:
        """
        params = {
            'limit': '50',
        }

        response = requests.get(
            url=f'{self.host}/api/v2/messages',
            params=params,
        )
        items = response.json()['items']
        return items

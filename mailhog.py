import pprint
import re
import requests
import ast

def post_v2_messages():
    params = {
        'limit': '50',
    }

    response = requests.get(
        url='http://localhost:5025/api/v2/messages',
        params=params,
    )
    json_string = response.json()['items'][0]['Content']['Body']
    activation_token = json_string.split('/')[-1][:-2]

    # print(ast.literal_eval(json_string)['ConfirmationLinkUrl'].split('/')[-1])
    # print(activation_token)
    # result = (re.search('activate/.*\"', json_string).group(0))
    # print(result[9:-1])
    return activation_token

print(post_v2_messages())

# int_ = 1
# float_ = 1.1
# str_ = 'string'
# tuple_ = 1, 2, 3, '4'
# list_ = [1, 2, 3, '4']
# dict_ = {
#     'key': 'value',
#     1: 'value',
#     (1, 2): 1,
#     2: [1, 3, 4],
#     'orders': [
#         {
#             'order': 1,
#             'price': 1000
#         },
#         {
#             'order': 1,
#             'price': 999
#         },
#     ]
# }
#
# print(dict_[2])
# print(dict_[2][2])
# print(response)
# print(response.headers)
# print(response.text)
# print(response.status_code)
# print(response.content)
#
# print(response.request.headers)
# print(response.request.url)
# print(response.request.method)


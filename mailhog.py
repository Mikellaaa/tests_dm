import pprint
import re
import requests
import ast

params = {
    'limit': '50',
}

response = requests.get(
    url='http://localhost:5025/api/v2/messages',
    params=params,
)
activation_token = response.json()['items'][0]['Content']['Body']

print(ast.literal_eval(activation_token)['ConfirmationLinkUrl'].split('/')[-1])

# print(activation_token)
print(activation_token.split('/')[-1][:-2])
result = (re.search('activate/.*\"', activation_token).group(0))
print(result[9:-1])


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


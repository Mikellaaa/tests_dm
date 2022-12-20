import pytest
import structlog
from copy import deepcopy

from dm_api_account.login_api import LoginApi
from dm_api_account.mailhog_api import MailHogApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)

@pytest.fixture(scope='session')
def login_api():
    login = LoginApi(host='http://localhost:5051')
    return login

@pytest.fixture(scope='session')
def user_headers(login_api):
    login_credentials = {
        'login': 'new_user3',
        'password': 'new_user3',
        'rememberMe': True,
    }
    response = login_api.post_v1_account_login(login_credentials=login_credentials)
    headers = {
        'X-Dm-Auth-Token': response.headers['X-Dm-Auth-Token']
    }
    return headers

@pytest.fixture(scope='session')
def login_user(login_api):
    login_credentials = {
        'login': 'new_user3',
        'password': 'new_user3',
        'rememberMe': True,
    }
    response = login_api.post_v1_account_login(login_credentials=login_credentials)
    headers = {
        'X-Dm-Auth-Token': response.headers['X-Dm-Auth-Token']
    }
    auth_login_user = deepcopy(login_api)
    auth_login_user.set_headers(headers)
    return auth_login_user

@pytest.fixture
def mailhog():
    m = MailHogApi(host='http://localhost:5025')
    yield m
    m.delete_v2_messages()


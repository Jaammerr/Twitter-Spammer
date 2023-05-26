import time
import requests
import pyuseragents
import random
import warnings

from models import Credentials, ConfigData
from hashlib import md5
from logger_file import logger
from pySpintax import spin
from utils import get_spam_message, convert_links_to_usernames

warnings.filterwarnings("ignore")


class Twitter:
    def __init__(self, credentials: Credentials, thread_number: int, config_data: ConfigData):
        self.config_data = config_data
        self.thread_number = thread_number
        self.session = requests.Session()
        self.credentials = credentials
        self.usernames = []
        self.spam_message = get_spam_message()

    def __setup_session_proxies(self):
        proxy_str = f'{self.credentials.user}:{self.credentials.password}@{self.credentials.ip}:{self.credentials.port}'
        self.session.proxies = {
            'http': f'http://{proxy_str}',
        }

    def __setup_session_headers(self):
        self.session.headers.update({
            'User-Agent': pyuseragents.random(),
            'Origin': 'https://mobile.twitter.com',
            'Referer': 'https://mobile.twitter.com/',
            'x-twitter-active-user': 'yes',
            'x-twitter-auth-type': 'OAuth2Session',
            'x-twitter-client-language': 'en',
            'content-type': 'application/x-www-form-urlencoded'
        })

    def __setup_session_auth(self):
        response = self.session.get(
            'https://abs.twimg.com/responsive-web/client-web/main.f3ada2b5.js',
            verify=False,
            timeout=self.config_data.max_response_timeout
        )

        bearer_token = 'Bearer ' + response.text.split('const r="ACTION_FLUSH",i="ACTION_REFRESH')[-1].split(',l="d_prefs"')[0].split(',s="')[-1].split('"')[0]
        csrf_token = md5(random.randbytes(32)).hexdigest()
        auth = f"des_opt_in=Y; auth_token={self.credentials.auth_token}; ct0={csrf_token};"

        self.session.headers.update({
            'cookie': auth,
            'authorization': bearer_token,
            'x-csrf-token': csrf_token
        })

    def __setup_session(self):
        if self.config_data.use_proxy:
            self.__setup_session_proxies()

        self.__setup_session_headers()
        self.__setup_session_auth()


    def get_username_id(self, username: str) -> int | bool:
        response = self.session.get(
            f"https://api.twitter.com/1.1/users/show.json?screen_name={username}",
            timeout=self.config_data.max_response_timeout
        )

        if response.status_code == 200:
            return int(response.json()['id'])

        else:
            return False


    def send_messages(self):
        for username in self.usernames:

            user_id = self.get_username_id(username=username)
            if user_id:

                spin_message = spin(self.spam_message)
                json_data = {
                    "event": {
                        "type": "message_create",
                        "message_create": {
                            "target": {
                                "recipient_id": f"{user_id}"
                            },
                            "message_data": {
                                "text": f"{spin_message}"
                            }
                        }}
                }

                response = self.session.post(
                    f'https://api.twitter.com/1.1/direct_messages/events/new.json',
                    json=json_data,
                    verify=False,
                    timeout=self.config_data.max_response_timeout
                )

                if response.status_code == 200:
                    logger.success(f'Thread №{self.thread_number} | Username: {username} | Message sent')

                else:
                    if 'errors' in response.text:

                        for error in response.json()['errors']:
                            logger.error(f'Thread №{self.thread_number} | Username: {username} | Failed to send message | Error message: {error["message"]} | Error code: {error["code"]} ')

                    else:
                        logger.error(f'Thread №{self.thread_number} | Username: {username} | Failed to send message')

            else:
                logger.error(f'Thread №{self.thread_number} | Username: {username} | Failed to get user_id')

            time.sleep(self.config_data.delay_between_messages)

        else:
            logger.info(f'Thread №{self.thread_number} | Work is over')


    def start(self):
        logger.info(f'Thread №{self.thread_number} | Working')

        self.__setup_session()
        self.usernames = convert_links_to_usernames(file_path='./files_data/spam_links.txt')
        self.send_messages()

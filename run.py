import threading

from config import setup_config
from models import Credentials, ConfigData
from main import Twitter
from utils import verify_data_format_in_files



def start_client():
    with open('./files_data/accounts_data.txt', 'r') as fp:
        accounts_data: list = [f.strip() for f in fp.readlines()]

    thread_number = 1
    thread_list = []

    for account_data in accounts_data:
        credentials = Credentials()

        try:
            credentials.auth_token, credentials.ip, credentials.port, credentials.user, credentials.password = account_data.split(':')

        except ValueError:
            credentials.auth_token = account_data.strip()


        client = Twitter(
            credentials=credentials,
            thread_number=thread_number,
            config_data=config_data
        )

        thread = threading.Thread(target=client.start, args=())
        thread_list.append(thread)
        thread_number += 1

    for thread in thread_list:
        thread.start()




if __name__ == '__main__':
    config_data: ConfigData = setup_config()
    verify_data_format_in_files(use_proxy=config_data.use_proxy)

    start_client()

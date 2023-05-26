import inquirer

from colorama import Style, Fore
from models import ConfigData


def setup_config() -> ConfigData:
    choices = [
        'Yes',
        'No',
    ]

    print(Fore.CYAN + Style.BRIGHT + 'Use arrows to move, type to filter\n' + Style.RESET_ALL)
    questions = [
        inquirer.List(
            'choice',
            message='Use a proxy',
            choices=choices,
            carousel=True
        )
    ]

    answers = inquirer.prompt(questions)
    __choice_of_proxy = answers['choice']
    config_data = ConfigData()

    while True:
        delay_question = inquirer.Text('delay', message='Enter delay between messages in seconds'),
        answers = inquirer.prompt(delay_question)

        __delay_between_messages = answers['delay']
        if not __delay_between_messages or not __delay_between_messages.isdigit():
            print(Fore.RED + Style.BRIGHT + 'ERROR | Incorrect delay\n' + Style.RESET_ALL)

        else:
            config_data.use_proxy = True if __choice_of_proxy == 'Yes' else False
            config_data.delay_between_messages = int(__delay_between_messages)

            break


    while True:
        response_timeout_question = inquirer.Text('response_timeout', message='Enter the maximum time in seconds to wait for a request response'),
        answers = inquirer.prompt(response_timeout_question)

        __response_timeout = answers['response_timeout']
        if not __response_timeout or not __response_timeout.isdigit():
            print(Fore.RED + Style.BRIGHT + 'ERROR | Incorrect time\n' + Style.RESET_ALL)

        else:
            config_data.max_response_timeout = int(__response_timeout)
            return config_data

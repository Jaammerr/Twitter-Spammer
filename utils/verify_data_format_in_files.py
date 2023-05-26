import os
import re
import sys

from colorama import Style, Fore


def verify_data_format_in_files(use_proxy: bool):
    os.system('cls')
    files_names: list = ['accounts_data.txt', 'spam_links.txt', 'spam_message.txt']

    for file_name in files_names:

        if os.path.exists(f'./files_data/{file_name}'):
            if os.stat(f'./files_data/{file_name}').st_size != 0:

                if file_name == 'spam_message.txt':
                    with open(f'./files_data/{file_name}', 'r', encoding='utf-8') as file:
                        spam_message = file.read()

                    stack = []
                    opening_brace = '{'
                    closing_brace = '}'

                    for char in spam_message:
                        if char == opening_brace:
                            stack.append(char)
                        elif char == closing_brace:
                            if len(stack) == 0:
                                return False
                            stack.pop()

                    if not len(stack) == 0:
                        print(Fore.RED + Style.BRIGHT + f'ERROR |  File {file_name} | You forgot to close the curly braces in the message' + Style.RESET_ALL)
                        sys.exit(0)


                else:
                    with open(f'./files_data/{file_name}', 'r', encoding='utf-8') as file:
                        lines = file.readlines()

                    for line in lines:

                        if file_name == 'accounts_data.txt':

                            if not use_proxy:
                                continue

                            else:
                                elements = line.strip().split(':')

                                if len(elements) != 5:
                                    print(Fore.RED + Style.BRIGHT + f'ERROR |  File {file_name} | The string {line} is not in the correct format' + Style.RESET_ALL)
                                    sys.exit(0)


                        elif file_name == 'spam_links.txt':
                            pattern = r'^https://twitter\.com/[\w-]+$'

                            line = line.strip()
                            if re.match(pattern, line):
                                continue

                            else:
                                print(Fore.RED + Style.BRIGHT + f'ERROR | File {file_name} | The link {line} is not in the correct format' + Style.RESET_ALL)
                                sys.exit(0)



            else:
                print(Fore.RED + Style.BRIGHT + f'ERROR | File {file_name} is empty' + Style.RESET_ALL)
                sys.exit(0)
        else:
            print(Fore.RED + Style.BRIGHT + f'ERROR | File {file_name} is not exists' + Style.RESET_ALL)
            sys.exit(0)

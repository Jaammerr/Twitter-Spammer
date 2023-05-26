def get_spam_message() -> str:
    with open('./files_data/spam_message.txt', 'r') as file:
        message = file.read()

    return message

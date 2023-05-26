


def convert_links_to_usernames(file_path: str) -> list[str]:
    usernames = []

    with open(file_path, 'r', encoding='utf-8') as file:
        links = file.readlines()

    for link in links:
        link = link.strip('\n')
        username = link.split('/')[3]
        usernames.append(username)

    return usernames


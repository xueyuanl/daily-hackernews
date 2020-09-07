import requests

import tokens


def create_issue(title, body, milestone=None, labels=None, assignees=None):
    url = 'https://api.github.com/repos/xueyuanl/daily-hackernews/issues'

    headers = {'Content-Type': 'application/json', 'Authorization': 'token ' + tokens.token}
    body = {'title': title, 'body': body}
    result = requests.post(url=url, json=body, headers=headers)

    if result.status_code == 201:
        return True
    return False


def main():
    create_issue('title', 'body')


if __name__ == '__main__':
    main()

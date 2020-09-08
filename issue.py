import json
import os

import requests


def create_issue(title, body, milestone=None, labels=None, assignees=None):
    url = 'https://api.github.com/repos/xueyuanl/daily-hackernews/issues'

    headers = {'Content-Type': 'application/json', 'Authorization': 'token ' + os.getenv('ACCESS_TOKEN')}
    body = {'title': title, 'body': body}
    result = requests.post(url=url, json=body, headers=headers)

    if result.status_code == 201:
        j_str = result.text
        issue_obj = json.loads(j_str)
        return issue_obj['url']
    return False


def lock_issue(issue_url):
    url = issue_url + '/lock'
    headers = {'Accept': 'application/vnd.github+json',
               'Authorization': 'token ' + os.getenv('ACCESS_TOKEN')}
    body = {'lock_reason': 'too heated'}
    result = requests.put(url=url, json=body, headers=headers)
    if result.status_code == 204:
        return True
    return False


def main():
    lock_issue('1')


if __name__ == '__main__':
    main()

import json

import requests


def get_top_stories(top_number=25):
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'

    result = requests.get(url=url)
    if result.status_code == 200:
        stories_list = str2list(result.text)[0:top_number]
        return stories_list
    raise Exception('Failed to get top stories with error code: ' + result.status_code)


def get_topic_item(id):
    url = 'https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'.format(id)
    result = requests.get(url=url)
    if result.status_code == 200:
        j_str = result.text
        topic_obj = json.loads(j_str)
        return topic_obj
    raise Exception('Failed to get topic item with error code: ' + result.status_code)


def str2list(s):
    if not s:
        return []
    temp = s[1:-1]
    return temp.split(',')


def main():
    stories = get_top_stories()
    for s in stories:
        item = get_topic_item(s)
        print(item)


if __name__ == '__main__':
    main()

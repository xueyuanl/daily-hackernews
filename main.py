import datetime
import re

from mdutils.mdutils import MdUtils

from hacker_news import get_top_stories, get_topic_item
from issue import create_issue, lock_issue


def url_parser(url):
    """
    get domain
    :return: str
    """
    m = re.search('https?://([A-Za-z_0-9.-]+).*', url)
    return m.group(1)


def get_date():
    current_time = datetime.datetime.now()
    return '{}-{}-{}'.format(str(current_time.day).zfill(2), str(current_time.month).zfill(2), current_time.year)


mdFile = MdUtils(file_name='hacker_news', title='temp')

mdFile.new_header(level=1, title='Daily Hacker News')  # style is set 'atx' format by default.
stories = get_top_stories()
for i, v in enumerate(stories):
    item = get_topic_item(v)
    id = item['id']
    title = item['title']
    url = item.get('url', None)
    if url:
        domain = url_parser(url)
        mdFile.new_line('{}. {} `{}` [`comments`](https://news.ycombinator.com/item?id={})'.format(
            str(i + 1), mdFile.new_inline_link(link=url, text=title, bold_italics_code='b'), domain, str(id)))
    else:
        link = 'https://news.ycombinator.com/item?id={}'.format(str(id))
        mdFile.new_line('{}. {} [`comments`]({})'.format(
            str(i + 1), mdFile.new_inline_link(link=link, text=title, bold_italics_code='b'), link))

issue_body = mdFile.file_data_text
date = get_date()
issue_url = create_issue('Daily Hacker News {}'.format(date), issue_body)
if not lock_issue(issue_url):
    raise Exception('Failed to lock issue {}, please lock it manually.'.format(issue_url))

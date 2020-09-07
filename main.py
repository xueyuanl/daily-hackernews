import re

from mdutils.mdutils import MdUtils

from hacker_news import get_top_stories, get_topic_item
from issue import create_issue


def url_parser(url):
    """
    get domain
    :return: str
    """
    m = re.search('https?://([A-Za-z_0-9.-]+).*', url)
    return m.group(1)


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
create_issue('daily Hacker News - test', issue_body)

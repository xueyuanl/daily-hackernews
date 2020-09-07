from mdutils.mdutils import MdUtils

from hacker_news import get_top_stories, get_topic_item
from issue import create_issue

mdFile = MdUtils(file_name='Example_Markdown', title='Markdown File Example')

mdFile.new_header(level=1, title='Daily Hacker News')  # style is set 'atx' format by default.

stories = get_top_stories()
for s in stories:
    item = get_topic_item(s)
    title = item['title']
    url = item['url']
    mdFile.new_line(' - ' + mdFile.new_inline_link(link=url, text=title))

issue_body = mdFile.file_data_text
create_issue('daily news', issue_body)

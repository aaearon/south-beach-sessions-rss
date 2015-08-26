import json
import os
from feedgen.feed import FeedGenerator
import sys

TITLE = 'The Dan LeBatard Show with Stugotz: South Beach Sessions'
LINK = 'http://espn.go.com/espnradio/story/_/id/11756027/south-beach-sessions'
DESCRIPTION = 'Listen to exclusive interviews with Dan and Stugotz.'
IMAGE_URL = 'http://a.espncdn.com/photo/2014/1106/radio_lebatardstugotz_576x324.jpg'
CONTACT = {'name': 'Tim Schindler',
           'email': 'tim.schindler@gmail.com'}


def generate_feed(input_file, output_file):
    fg = FeedGenerator()
    fg.load_extension('podcast', rss=True)

    ## RSS tags
    # Required
    fg.title(TITLE)
    fg.link(href=LINK)
    fg.description(DESCRIPTION)
    # Optional
    fg.language('en')
    fg.image(url=IMAGE_URL, title=TITLE, link=LINK)
    fg.ttl(720)
    fg.webMaster(CONTACT['name'])
    # iTunes
    fg.podcast.itunes_author('Dan LeBatard')
    fg.podcast.itunes_category(itunes_category='Sports & Recreation', itunes_subcategory='Professional')
    fg.podcast.itunes_image(itunes_image=IMAGE_URL)
    fg.podcast.itunes_explicit(itunes_explicit='clean')
    fg.podcast.itunes_owner(name=CONTACT['name'], email=CONTACT['email'])

    # Add items
    items = read_items(input_file)
    for item in items:
        fe = fg.add_entry()

        ## RSS tags
        fe.id(item['guid'])
        fe.title(item['title'])
        fe.description(item['description'])
        fe.enclosure(item['link'], 0, 'audio/mpeg')
        fe.pubdate(item['pubDate'])

    # Finish off the file
    fg.rss_str(pretty=True)
    fg.rss_file(output_file)


def read_items(file=file):
    with open(file) as json_file:
        items = json.load(json_file)
    return items


if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if os.path.exists(input_file):
        generate_feed(input_file, output_file)


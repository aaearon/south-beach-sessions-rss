south-beach-sessions-rss
========================

The goal is to take the South Beach Sessions interviews from The Dan LeBatard Show and Stugotz (http://espn.go.com/espnradio/story/_/id/11756027/south-beach-sessions) and produce a RSS/podcast file to be used within a media player.

Generate yourself or use daily-generated feed at `http://iosharp.com/podcasts/sbs.xml`

###Install Requirements
`pip install -r requirements.txt`

###Usage
Scrape the audio files and store as JSON objects

`scrapy crawl sbs -t json -o /tmp/items.json`

Generate the RSS XML

`python generate_rss_xml.py /tmp/items.json podcast.xml`


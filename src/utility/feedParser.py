# Feed from RSS or News API will be processed through this file and then distributed to the "front" of the code.
# System/Bot will be posting news articles automatically.
# SQLite for deduplication WIP

# REQUIRED INFORMATION TO PARSE/HADLE FOR EMBED
# TITLE
# DESCRIPTION
# IMAGE
# ARTICLE URL
# AUTHOR URL (IF PROVIDED)
# DATE PUBLISHED
# ?? FOOTER TEXT


# RSS provides all 4.
import feedparser
import re

feed = 'https://rss.app/feeds/tU4QxjXvV6DFf7Rl.xml'
incoming = feedparser.parse(feed)

def get_Image(source):
    proc = incoming.entries[0].summary

    # Specific re(Regex) is made to work with RSS. Unknown if it works with other feeds.
    match = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', proc)
    print(match.group(1))

    return image

# Not Final.
# For testing, only the first entry will be sent
# Thinking of using .get() for the entries information rather than the .title and etc
title = incoming.entries[0].title
description = incoming.entries[0].description
image = incoming.entries[0].link
link = incoming.entries[0].link
author = incoming.entries[0].author
date = incoming.entries[0].published #published_parsed
imgSource = incoming.entries[0].summary


print(title)
print("---------------------------------")
print(description)
print("---------------------------------")
print(link)
print("---------------------------------")
print("Author is " + author)
print("---------------------------------")
print(date)
print("---------------------------------")
get_Image(imgSource)
# Feed from RSS or News API will be processed through this file and then distributed to the "front" of the code.
# System/Bot will be posting news articles automatically.
# SQLite for deduplication WIP
import feedparser

incoming = feedparser.parse('https://rss.app/feeds/tU4QxjXvV6DFf7Rl.xml')

title = incoming.entries[0].title
description = incoming.entries[0].description
link = incoming.entries[0].link

print(title)
print(description)
print(link)
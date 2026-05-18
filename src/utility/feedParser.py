# Feed from RSS or News API will be processed through this file and then distributed to the "front" of the code.
# System/Bot will be posting news articles automatically.
# SQLite for deduplication WIP
import feedparser

incoming = feedparser.parse('https://rss.app/feeds/tU4QxjXvV6DFf7Rl.xml')

parsedInfo = incoming

print(parsedInfo)
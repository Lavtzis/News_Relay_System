import feedparser

d = feedparser.parse('https://rss.app/feeds/tU4QxjXvV6DFf7Rl.xml')
d['feed']['title']

print(d)
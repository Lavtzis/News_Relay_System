import logging

def logger():
    debug_handler = logging.FileHandler(filename='discord_news_debug.log', encoding='utf-8', mode='w')
    debug_handler.setLevel(logging.DEBUG)

    main_handler = logging.FileHandler(filename='discord_news.log', encoding='utf-8', mode='w')
    main_handler.setLevel(logging.INFO)

    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s", handlers=[debug_handler, main_handler])
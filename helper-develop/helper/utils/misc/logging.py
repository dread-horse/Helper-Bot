import logging

logging.basicConfig(handlers=[logging.FileHandler(
    'log.txt', 'w', 'utf-8')], level=logging.INFO)


# input info from https://my.telegram.org/
from telethon import TelegramClient, events, sync

session_name = 'scraper'
api_id = 11111111
api_hash = 'api_hash'

client = TelegramClient(session_name, api_id, api_hash)
client.start()
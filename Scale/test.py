from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest

api_id = '[DELETED]'  # substitute with your value
api_hash = '[DELETED]'  # substitute with your value
channel_username = '[DELETED]'  # substitute with your value

with TelegramClient('anon', api_id, api_hash) as client:
    posts = client(GetHistoryRequest(
        peer=channel_username,
        limit=100,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0))

    for message in posts.messages:
        print(message)

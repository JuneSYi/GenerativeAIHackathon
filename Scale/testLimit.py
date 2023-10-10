# scrapes up to 1000 messages

from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest

api_id = '[DELETED]'  # substitute with your value
api_hash = '[DELETED]'  # substitute with your value
channel_username = '[DELETED]'  # substitute with your value

with TelegramClient('anon', api_id, api_hash) as client:
    last_message_id = 0
    total_messages = 0
    while True:
        history = client(GetHistoryRequest(
            peer=channel_username,
            limit=100,
            offset_date=None,
            offset_id=last_message_id,
            max_id=0,
            min_id=0,
            add_offset=0,
            hash=0
        ))
        if not history.messages:
            break
        for message in history.messages:
            print(message)
            total_messages += 1
            if total_messages >= 1000:
                break
        if total_messages >= 1000:
            break
        last_message_id = history.messages[-1].id

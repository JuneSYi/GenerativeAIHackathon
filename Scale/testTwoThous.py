from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest

api_id = '[DELETED]'  # substitute with your value
api_hash = '[DELETED]'  # substitute with your value
channel_username = '[DELETED]'  # substitute with your value

with TelegramClient('anon', api_id, api_hash) as client:
    offset_id = 0
    limit = 2000
    all_messages = []
    while len(all_messages) < limit:
        history = client(GetHistoryRequest(
            peer=channel_username,
            limit=100,
            offset_date=None,
            offset_id=offset_id,
            max_id=0,
            min_id=0,
            add_offset=0,
            hash=0
        ))
        if not history.messages:
            break
        all_messages.extend(history.messages)
        offset_id = all_messages[-1].id
    print(all_messages[:limit])

from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import MessageEntityTextUrl, MessageEntityHashtag

api_id = '[DELETED]'  # substitute with your value
api_hash = '[DELETED]'  # substitute with your value
channel_username = '[DELETED]'  # substitute with your value

with TelegramClient('anon', api_id, api_hash) as client:
    history = client(GetHistoryRequest(
        peer=channel_username,
        limit=1,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0
    ))
    message = history.messages[0]
    # print(message)

    print(f"Message ID: {message.id}")
    print(f"Chat ID: {message.peer_id.channel_id}")
    print(f"Date: {message.date}")
    print(f"Text: {message.message}")
    print("##############")
    # Print out the URLs and hashtags in the message
    for entity in message.entities:
        if isinstance(entity, MessageEntityTextUrl):
            print(f"URL: {entity.url}")
        if isinstance(entity, MessageEntityHashtag):
            offset, length = entity.offset, entity.length
            print(f"Hashtag: {message.message[offset:offset+length]}")


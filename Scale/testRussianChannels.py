from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import SearchRequest
from telethon.tl.types import InputPeerSelf

api_id = '[DELETED]'  # substitute with your value
api_hash = '[DELETED]'  # substitute with your value

with TelegramClient('anon', api_id, api_hash) as client:
    result = client(SearchRequest(
        q='Группа Вагнера',  # This is 'Wagner Group' in Russian
        limit=100
    ))

    for chat in result.chats:
        print(chat.title)
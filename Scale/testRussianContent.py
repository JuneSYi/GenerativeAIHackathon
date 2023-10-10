from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import MessageEntityTextUrl, MessageEntityHashtag
import telethon

api_id = '[DELETED]'  # substitute with your value
api_hash = '[DELETED]'  # substitute with your value

def search_for_russian_channels():
    # Create a Telegram client
    client = telethon.TelegramClient('anon', api_id="[DELETED]", api_hash="[DELETED]")

    # Search for channels that contain Russian language in the contents
    result = client.get_messages(
        "#general",
        limit=100,
        q="russian"
    )

    # Print the results
    for channel in result:
        print(channel.title)

if __name__ == "__main__":
    search_for_russian_channels()
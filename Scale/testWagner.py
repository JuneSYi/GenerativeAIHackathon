# Группа Вагнера

import json
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import MessageEntityTextUrl, MessageEntityHashtag

api_id = '[DELETED]'  # substitute with your value
api_hash = '[DELETED]'  # substitute with your value
channel_username = '[DELETED]'  # substitute with your value

with TelegramClient('anon', api_id, api_hash) as client:
    last_message_id = 0
    total_messages = 0
    messages_list = []  # list to store the messages
    while total_messages < 1000:
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
            # Create a dictionary for each message
            temp = message.message
            tempList = []
            if message.entities is not None:
                for entity in message.entities:
                    if isinstance(entity, MessageEntityTextUrl):
                        if entity.url[-4:] == ".jpg":
                            tempList.append(entity.url)
                        # print(f"URL: {entity.url}")
            jpgExists = False
            urlStrings = ""
            if len(tempList) > 0:
                jpgExists = True
                for val in tempList:
                    urlStrings = urlStrings + "URL: " + val + " "
            if jpgExists:
                msg_dict = {"text": message.message, "url": urlStrings, "title": message.id}
            else:
                msg_dict = {"text": message.message, "url": "", "title": message.id}
            messages_list.append(msg_dict)
            total_messages += 1
            if total_messages >= 1000:
                break
        last_message_id = history.messages[-1].id

    with open('outputWagner.txt', 'w', encoding='utf8') as f:
        # Dump the list of messages (dictionaries) into the file
        json.dump(messages_list, f, ensure_ascii=False, indent=4)

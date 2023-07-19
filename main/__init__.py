#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 26670684
API_HASH = "60592bded0f25a9633a8133601f2c779"
BOT_TOKEN = "6289264953:AAG1N1Q3_KXM-V2KB-nDb9LFlMXq9WpZPv8"
SESSION = "BQGW9lwAExVt4H5FtCfx4r3jeUoe83P9STo7lagHU59paZHMnd4nWjuOIYPPyUU6o4NYYFVoUBu1nr_QWcR9JOgd51wh3cGEpxoadayO4eH9tEL-0AWqF_m5tmlgEli3W67aGBa9TC7zqfvd0NibSuzRwUfA0xerutSnUxVp3zUKLiCPfMI55zJBJvvYO9096_Db3gCzy0Ci4V5pOCqKopIctBu9s2ZsnyOJu0FSAYNq96i-V-f4VkMAYfYfJJsR46IR6QGJ9wY2RVjuoBRm76ppf08eXcAJSBWxu8Y-nhjp6K8j1CXbBobQvT7EZtZdG2OvTk9LTpFQQxDCty6XSX8UtaxxdQAAAAFobLnbAA"
FORCESUB = "adult_updates"
AUTH = "6046923227"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)

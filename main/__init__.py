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
BOT_TOKEN = "6317945060:AAE8VqjA0HGWu23EtN4OBmGuPjMb7ttHZYI"
SESSION = "BQBViF58NtXuM8iP4GSdIMlP0ZRIAqA8bF6yk64VVyZCkjp4r-kA7iVyOTbkKJdQGpwNkcBd0dDEniMzNVqzzUhzjAfUg6ml8WgF7n8QkmPk0KnapvwoEbgvn4pSEQXxQtJeOrlb610XsrltWCMMJ72bI1Hj5BoHNQv8ms0OUSRHuXeCnAVuvhc5cFedGzvPmzi1IxNd4iygVe4nx7pWfVwqx34F8Nlfh1NtUXiOeLumjbbTsbh75VMMi9Op8XZB9PFasFE2Gl3w9YzZgEg37RYkTjCdRxnnIL0IgBSk1vufGICvUGtBdRqsn1hCh8Ug13MkANfTQM3XMbkf8ls4743qAAAAAYGt698A"
FORCESUB = "adult_updates"
AUTH = "6470626271"

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

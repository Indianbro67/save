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
BOT_TOKEN = "6289264953:AAGXNmL3GruFdPDTitjPpGgAKIwG4MxA9Zs"
SESSION = "BQB8EdI-9AwgAGhnmVbU5H7lE4742ENWHZtkF7_RwCnu5guTqBEbCoGevhpa4QhPuobYUDx6yPOy9XxD3jCtLXf9GKjZsapnuJxax12--LJ5gNFQcQCsAg55rHcZNKo45CSgv2aURNbwf8FrRIAey2gCPvvlhLELsU9oxv-ibuwYBH7gEJzlim4axXqowBDbE27iqGOfip1NDXiw6cu77noWzWsHQFrpHlHDQCtJXDrQrJPNcXeRsNWskR9LjzJRypMXMxlVNzbLlWLGvuXb4lWqxSmuXyhX5kH52RXlL5hCDK3oT9Wtpln2HYrVxgfsBV1ocBZUz9ifR2gYLgmtIykOAAAAAWhsudsA"
FORCESUB = "op_bro_official_group"
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

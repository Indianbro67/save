#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 22611629
API_HASH = "762265a63c3c56717476a2c74d7f7acc"
BOT_TOKEN = "5835400119:AAG05VIHGiaNvefr3DKF4yd8bTAcZLSyxx4"
SESSION = "AQB0B1Kxzz8U_J7oDHfnCNWWdxNQOqq6WHKEvm_i8C6VL5n2f7tWeS-GFsL5jJ_o_-loLjfObNdYD8LmcoSuLcqkH5yPHvxqTHoSrVmZomIUlBfvjcVDN0YcaavW1-z3ezP9vLrBsw4dKNSTjJpsHHljaez8Tfix3vqPO7DNCP16IRTr2SW6sHqLyl6Vn35n0ay8x12eDKYqQpqG3esymMogUoss2Dcs1nVW9D_Quuea-7IkyoCuk9SP3_ZxmXxI1ukDIBVsGA8QrZyyqjOuUQohdxFThrvFNwIDhY17_lDOfzChtBkeGzfNuOtKHTwRh8wGd8TzNHa0bVbWH-yOSil0AAAAAWvVxDkA"
FORCESUB = "adult_chatting_groupxx"
AUTH = "5841005593"

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

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
SESSION = "BQB_7VmvtLpC_qAThmGwwvY7VSEO8HBFwVr2U8Yv0boD3U89l_ydKbZjsI4BnaWutkXorRbpCtTL-p1qW8lXs-utVZqWC9Gn9rHfCcnwVqUCF_xSTFqKrzP4IP0g8e0dauCgHqSVASwu01DNnT06Zvso-P8WUEF4M060MOxMm07U5MvQpJRxyCDRe3Qo3CbuqNjLVrPuBLlC5XCudfh4p0E3Up1aIHTt4jWpq9o5TjtCIGKqAm5VC5DQcw84W-hECulCpiRhkj9QU0iEiM-zzr8RH3YgJrztmwSC-B9R1nrCJypLjoNgIcyAGNwJwwlGF6bVjeZ05SvCOTtcMtnhdaaRAAAAAWppYSUA"
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

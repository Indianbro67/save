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
SESSION = "BQGW9lwAP6bI-dEkKKwBtkR4MgcttQ8XwZT6cjD7ULcdrfOT80KPxpxfs9LeJQnYFsSqI0Qsztr1_EliOE3lpe-JRGLPOlXnFvgVxLedajXhJWHuNXbu_4OuOqvT0jagqQqF-OzQ1ovoK6D00pugJkr6YljPmd1kCDPjXtpEmqgW2rePZNSqjCIlbAI-1Q0LwkW1HlO8cHwRQw9VGj3TPW_CAMIruxvkakz2JNDYdDITMbtOXQafu33gAtts6EAkEYF_01YcHu9X8kzlUpBL1G0UiSc2kX2FEnx3cCvuj-c5eC4MWHYInhkdi7d3zruvB43liyBpcftrNViCbU1jsPYyyzqQmgAAAAFobLnbAA"
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

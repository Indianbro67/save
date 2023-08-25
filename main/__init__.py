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
BOT_TOKEN = "5835400119:AAG05VIHGiaNvefr3DKF4yd8bTAcZLSyxx4"
SESSION = "BQGMcpgARhlnkzCl_IyyNbYgrP8nwzKXubPU1XCzNBpjYI_0m-Zu5W_khEvXXEQjZ_4gSl1WhYVpJ1wmkGA4Y6wiJlKHdZ2Jw01ArKSJGv-A30fhUFuq0sMP338FzeJ0i7i8D-LP-rr6ztje3zmmc-mF_dlWLJrrKjZhB2vNDLwZDQtwbUC6-7KW-q2df7IqNUW-7YHU203x4btr5YBEosYRZc64MV7LG1050EZO38D7HAyJt5aM1RFMElGS1Mha5uf989yfrEorTUnQD9hoBSMHpchv1S0w1EZnbIr5NIbPotUQiDcKXZUyfml_nEE_pgr3iKBTdlRfG99apLkWhRhTDCTqCAAAAAFjb9EKAA"
FORCESUB = "adult_girls_xxx"
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

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
SESSION = "BQGMcpgAKXYTi9nCVQOo8d6DDnBlaJnihDYEQ6oYBNBLfKWy9K7fLRfgCjWQ3Px-GDZn5YUZFhSv4Rjtu3EGFD4QjjSYZAy3Rf1bvYh6Ey5uGGR4QNtWtyhP8HMOGDK45rDukpZhsjvoas9aaKlNPJT9B-1cLb8ToDBssJ-apcZWHM7pPqvuWRJuiuQxoSX3l-oAtbRt1o3aoSVaYEgHJ_LaeMnVaUrRkYpd3XgjauLBGwtMGl-s6NwrrI1r8w6ddXgyx5Yflwy5obvpdHk09EdYClYYxvVJ8IHVm13VC2B-r56-g34anjR81J1t42YiYZOB0jlQF9PWIJOwXINaV1QIg9qxBAAAAAFcJqwZAA"
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

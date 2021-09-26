import requests
from pyrogram import Client as Bot

from InnexiaMusic.config import API_HASH, API_ID, BG_IMAGE, TOKEN
from Innexia.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./image/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=TOKEN,
    plugins=dict(root="plugins"),
)


START_TEXT = """
Hello {}, I am Telegram calculator bot 
 Send me /calc or /claculator and See what can I do!.
My creator [@Shoto_GirlFriend_777](https://t.me/Shoto_GirlFriend_777/604)
"""
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Join my group 💗', url='https://t.me/animefan_club777'),
        InlineKeyboardButton('Channel 📢', url='https://t.me/moviesebseriesAnimes')
        ]]
    )

bot.start()
run()
